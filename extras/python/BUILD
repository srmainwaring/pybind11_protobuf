#------------------------------------------------
# Python examples

py_binary(
  name = "vector3d_example",
  main = "vector3d_example.py",
  srcs = ["vector3d_example.py"],
  data = [
      "@com_google_protobuf//:proto_api",
  ],
  deps = [
      "//extras/msgs:vector3d_py_pb2",
  ],
)

py_binary(
  name = "pose_example",
  main = "pose_example.py",
  srcs = ["pose_example.py"],
  data = [
      "@com_google_protobuf//:proto_api",
  ],
  deps = [
      "//extras/msgs:pose_py_pb2",
  ],
)
