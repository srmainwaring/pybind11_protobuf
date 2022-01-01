'''
Example using the extra.msgs.vector3d protobuf
'''

from extras.msgs.pose_pb2 import Pose

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


if __name__ == "__main__":
  main()