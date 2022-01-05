'''
Example using the extras.msgs.pose protobuf
'''

from extras.msgs.pose_pb2 import Pose
from extras.msgs.vector3d_pb2 import Vector3d

from google.protobuf.internal import api_implementation

def main():
  print("Pose Example")
  print("============")

  #----------------------------------------------
  # check google.protobuf implementation
  print("\ngoogle.protobuf implementation")
  print("------------------------------")
  print(api_implementation.Type())

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

  #----------------------------------------------
  # native Python protobuf
  print("\npy vector3d")
  print("-----------")
  pos = Vector3d()
  pos.x = 53.1
  pos.y = 23.7
  pos.z = 10.2
  print("{}".format(msg))
  print("isinstance: {}".format(isinstance(pos, Vector3d)))

  print("\npy pose.position.CopyFrom py vector3d")
  print("-------------------------------------")
  msg.position.CopyFrom(pos)
  print("{}".format(msg))
  print("isinstance: {}".format(isinstance(msg, Pose)))


if __name__ == "__main__":
  main()
