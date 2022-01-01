load("@pybind11_bazel//:build_defs.bzl", "pybind_extension", "pybind_library")

#------------------------------------------------
# C++ library

cc_library(
    name = "extras_lib",
    srcs = ["src/extras.cc"],
    hdrs = ["src/extras.hh"],
  deps = [
      "//extras/msgs:vector3d_cc_proto",
  ],
  visibility = ["//visibility:public"],
)

#------------------------------------------------
# Python C++ extension module

pybind_extension(
  name = "extras_module",
  srcs = ["src/extras_module.cc"],
  deps = [
      ":extras_lib",
      "//extras/msgs:vector3d_cc_proto",
      "//pybind11_protobuf:native_proto_caster",
      "@com_google_protobuf//:protobuf",
  ],
  visibility = ["//visibility:public"],
)
