#============================================================================
# External dependencies for pybind11_protobuf
# 
# protobuf is included as a submodule for the Python headers,
# but is not compiled 
# 
add_subdirectory(abseil-cpp)
# add_subdirectory(protobuf)
add_subdirectory(pybind11)
