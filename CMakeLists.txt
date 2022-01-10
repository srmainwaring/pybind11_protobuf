#============================================================================
# CMake file for pybind11_protobuf
# 
# See pybind11_protobuf/BUILD
cmake_minimum_required(VERSION 3.10.2 FATAL_ERROR)

project(pybind11_protobuf)

#============================================================================
# Options
set(ABSL_PROPAGATE_CXX_STD ON)
set(PYBIND11_FINDPYTHON ON)

#============================================================================
# Find Python
find_package(Python COMPONENTS Interpreter Development)

#============================================================================
# Find pybind11
# find_package(pybind11 CONFIG)

#============================================================================
# Find Protobuf
find_package(Protobuf)

#============================================================================
# External modules (abseil-cpp, pybind11)
add_subdirectory(external)

#============================================================================
# Debug messages for find_package

# message("pybind11_FOUND: ${pybind11_FOUND}")
# message("pybind11_VERSION: ${pybind11_VERSION}")
# message("pybind11_VERSION_TYPE: ${pybind11_VERSION_TYPE}")
# message("pybind11_INCLUDE_DIRS: ${pybind11_INCLUDE_DIRS}")
# message("pybind11_INCLUDE_DIR: ${pybind11_INCLUDE_DIR}")
# message("pybind11_DEFINITIONS: ${pybind11_DEFINITIONS}")
# message("pybind11_LIBRARIES: ${pybind11_LIBRARIES}")

# message("Python_FOUND: ${Python_FOUND}")
# message("Python_VERSION: ${Python_VERSION}")
# message("Python_INCLUDE_DIRS: ${Python_INCLUDE_DIRS}")
# message("Python_LIBRARIES: ${Python_LIBRARIES}")

# message("Protobuf_FOUND: ${Protobuf_FOUND}")
# message("Protobuf_VERSION: ${Protobuf_VERSION}")
# message("Protobuf_INCLUDE_DIRS: ${Protobuf_INCLUDE_DIRS}")
# message("Protobuf_LIBRARIES: ${Protobuf_LIBRARIES}")

#============================================================================
# pybind11_proto pybind11 extension module
pybind11_add_module(pybind11_proto MODULE
  pybind11_protobuf/proto.cc
  pybind11_protobuf/proto_utils.cc
  pybind11_protobuf/proto_utils.h
)

target_link_libraries(pybind11_proto
  PRIVATE
    absl::strings
    protobuf::libprotobuf
    ${Python_LIBRARIES}
)

target_include_directories(pybind11_proto
  PRIVATE
    ${PROJECT_SOURCE_DIR}
    ${Protobuf_INCLUDE_DIRS}
    ${pybind11_INCLUDE_DIRS}
)

#============================================================================
# pybind11_native_proto_caster shared library
add_library(pybind11_native_proto_caster SHARED
  pybind11_protobuf/enum_type_caster.h
  pybind11_protobuf/native_proto_caster.cc
  pybind11_protobuf/native_proto_caster.h
  pybind11_protobuf/proto_cast_util.cc
  pybind11_protobuf/proto_cast_util.h
  pybind11_protobuf/proto_caster_impl.h
)

target_link_libraries(pybind11_native_proto_caster
  absl::flat_hash_map
  absl::flat_hash_set
  absl::hash
  absl::strings
  absl::optional
  protobuf::libprotobuf
  pybind11::pybind11
  ${Python_LIBRARIES}
)

target_include_directories(pybind11_native_proto_caster
  PRIVATE
    ${PROJECT_SOURCE_DIR}
    ${PROJECT_SOURCE_DIR}/external/protobuf
    ${Protobuf_INCLUDE_DIRS}
    ${pybind11_INCLUDE_DIRS}
)

#============================================================================
# pybind11_wrapped_proto_caster shared library
add_library(pybind11_wrapped_proto_caster SHARED
  pybind11_protobuf/wrapped_proto_caster.h
  pybind11_protobuf/proto_cast_util.cc
  pybind11_protobuf/proto_cast_util.h
  pybind11_protobuf/proto_caster_impl.h
)

target_link_libraries(pybind11_wrapped_proto_caster
  absl::flat_hash_map
  absl::flat_hash_set
  absl::hash
  absl::strings
  absl::optional
  protobuf::libprotobuf
  pybind11::pybind11
  ${Python_LIBRARIES}
)

target_include_directories(pybind11_wrapped_proto_caster
  PRIVATE
    ${PROJECT_SOURCE_DIR}
    ${PROJECT_SOURCE_DIR}/external/protobuf
    ${Protobuf_INCLUDE_DIRS}
    ${pybind11_INCLUDE_DIRS}
)
