'''
Example using the extra.msgs.vector3d protobuf
'''

from extras.msgs.vector3d_pb2 import Vector3d

def main():
  print("Vector3d Example")
  print("================")

  print("\nCreate")
  print("------")
  msg = Vector3d()
  msg.x = 1.0
  msg.y = 2.0
  msg.z = 3.0
  print("{}".format(msg))

  print("IsInstance")
  print("----------")
  print("isinstance: {}".format(isinstance(msg, Vector3d)))


if __name__ == "__main__":
  main()