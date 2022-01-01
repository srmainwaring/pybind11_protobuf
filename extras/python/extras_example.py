'''
Example using the extras.msgs.pose protobuf
'''

from extras.msgs.pose_pb2 import Pose
from extras.msgs.vector3d_pb2 import Vector3d

from extras import extras_module as m

def main():
  print("Extras Module Example")
  print("===================")

  print("\ncpp vector3d")
  print("------------")
  msg = m.get_vector3d(1.0, 2.0, 3.0)
  print(msg)
  print("isinstance: {}\n".format(isinstance(msg, Vector3d)))
  msg = m.set_vector3d(msg)

  print("\npy vector3d")
  print("-----------")
  msg = Vector3d()
  msg.x = 53.1
  msg.y = 23.7
  msg.z = 10.2
  print(msg)
  print("isinstance: {}\n".format(isinstance(msg, Vector3d)))
  msg = m.set_vector3d(msg)

if __name__ == "__main__":
  main()

