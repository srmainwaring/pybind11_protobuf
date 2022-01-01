'''
Example using the extras.msgs.pose protobuf
'''

from extras.msgs.pose_pb2 import Pose
from extras.msgs.vector3d_pb2 import Vector3d

def main():
  print("Pose Example")
  print("============")

  print("\nCreate")
  print("------")
  msg = Pose()
  msg.position.x = 1.0
  msg.position.y = 2.0
  msg.position.z = 3.0
  print("{}".format(msg))

  print("IsInstance")
  print("----------")
  print("isinstance: {}".format(isinstance(msg, Pose)))

  print("\nCompose")
  print("-------")
  pos = Vector3d()
  pos.x = 53.1
  pos.y = 23.7
  pos.z = 10.2
  msg.position.CopyFrom(pos)
  print("{}".format(msg))


if __name__ == "__main__":
  main()
