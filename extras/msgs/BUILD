load("@com_github_grpc_grpc//bazel:python_rules.bzl", "py_proto_library")
load("@pybind11_bazel//:build_defs.bzl", "pybind_extension")

#------------------------------------------------
# generate protobuf bindings for C++ and Python

# vector3d.proto
proto_library(
    name = "vector3d_proto",
    srcs = [
      "vector3d.proto"
    ],
    visibility = ["//visibility:public"],
)

cc_proto_library(
    name = "vector3d_cc_proto",
    deps = [":vector3d_proto"],
    visibility = ["//visibility:public"],
)

py_proto_library(
    name = "vector3d_py_pb2",
    deps = [":vector3d_proto"],
    visibility = ["//visibility:public"],
)

# pose.proto
proto_library(
    name = "pose_proto",
    srcs = [
      "pose.proto"
    ],
    deps = [":vector3d_proto"],
    visibility = ["//visibility:public"],
)

cc_proto_library(
    name = "pose_cc_proto",
    deps = [":pose_proto"],
    visibility = ["//visibility:public"],
)

py_proto_library(
    name = "pose_py_pb2",
    deps = [":pose_proto"],
    visibility = ["//visibility:public"],
)
