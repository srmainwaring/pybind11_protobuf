'''
Example using the extras.msgs.pose protobuf
'''

from extras.msgs.pose_pb2 import Pose
from extras.msgs.vector3d_pb2 import Vector3d

from extras import extras_module as m

from google.protobuf.internal import api_implementation

def main():
  print("Extras Module Example")
  print("===================")

  #----------------------------------------------
  # check google.protobuf implementation
  print("\ngoogle.protobuf implementation")
  print("------------------------------")
  print(api_implementation.Type())

  #----------------------------------------------
  # native Python protobuf
  print("\npy vector3d")
  print("-----------")
  pos = Vector3d()
  pos.x = 53.1
  pos.y = 23.7
  pos.z = 10.2
  print("{}".format(pos))
  print("isinstance: {}".format(isinstance(pos, Vector3d)))

  # check pybind11 extension accepts native Python protobuf
  m.take_vector3d(pos)

  #----------------------------------------------
  # cpp wrapped protobuf
  print("\ncpp vector3d")
  print("------------")
  pos = m.make_vector3d(10.2, 53.1, 27.3)
  print("{}".format(pos))
  print("isinstance: {}".format(isinstance(pos, Vector3d)))

  # check pybind11 extension accepts cpp wrapped protobuf
  m.take_vector3d(pos)

  #----------------------------------------------
  # native Python protobuf
  print("\npy pose")
  print("-------")
  msg = Pose()
  msg.position.x = 1.0
  msg.position.y = 2.0
  msg.position.z = 3.0
  print("{}".format(msg))
  print("isinstance: {}".format(isinstance(msg, Pose)))

  # check pybind11 extension accepts native Python protobuf
  m.take_pose(msg)

  #----------------------------------------------
  # cpp wrapped protobuf
  print("\ncpp pose")
  print("--------")
  msg = m.make_pose(10.2, 53.1, 27.3)
  print("{}".format(msg))
  print("isinstance: {}".format(isinstance(msg, Pose)))

  # check pybind11 extension accepts cpp wrapped protobuf
  m.take_pose(msg)

  #----------------------------------------------
  print("\ncpp wrapped pose using cpp wrapped vector3d")
  print("---------------------------------------------")
  pos = m.make_vector3d(10.2, 53.1, 27.3)
  msg = m.make_pose(10.2, 53.1, 27.3)
  msg.position.CopyFrom(pos)
  print("{}".format(msg))
  print("isinstance: {}".format(isinstance(msg, Pose)))

  #----------------------------------------------
  # TODO: fix failing example
  print("\ncpp wrapped pose using native Python vector3d")
  print("---------------------------------------------")
  pos = Vector3d()
  pos.x = 10.2
  pos.y = 53.1
  pos.z = 27.3
  msg = m.make_pose(10.2, 53.1, 27.3)
  msg.position.CopyFrom(pos)
  print("{}".format(msg))
  print("isinstance: {}".format(isinstance(msg, Pose)))

  #----------------------------------------------
  # TODO: fix failing example
  print("\nnative Python pose using cpp wrapped vector3d")
  print("---------------------------------------------")
  pos = m.make_vector3d(10.2, 53.1, 27.3)
  msg = Pose()
  msg.position.CopyFrom(pos)
  print("{}".format(msg))
  print("isinstance: {}".format(isinstance(msg, Pose)))

if __name__ == "__main__":
  main()

