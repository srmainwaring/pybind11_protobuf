'''
Example using the extras.msgs.vector3d protobuf
'''

from extras.msgs.vector3d_pb2 import Vector3d

from google.protobuf.internal import api_implementation

def main():
  print("Vector3d Example")
  print("================")

  #----------------------------------------------
  # check google.protobuf implementation
  print("\ngoogle.protobuf implementation")
  print("------------------------------")
  print(api_implementation.Type())

  #----------------------------------------------
  # native Python protobuf
  print("\npy vector3d")
  print("-----------")
  msg = Vector3d()
  msg.x = 1.0
  msg.y = 2.0
  msg.z = 3.0
  print("{}".format(msg))
  print("isinstance: {}".format(isinstance(msg, Vector3d)))


if __name__ == "__main__":
  main()
