#include "extras.hh"

extras::msgs::Vector3d GetVector3d(double x, double y, double z)
{
  extras::msgs::Vector3d msg;
  msg.set_x(x);
  msg.set_y(y);
  msg.set_z(z);
  return msg;
}

void SetVector3d(const extras::msgs::Vector3d& msg)
{
  std::cout << "Set Vector3d" << std::endl;
  std::cout << "------------" << std::endl;
  std::cout << "x: " << msg.x() << std::endl;
  std::cout << "y: " << msg.y() << std::endl;
  std::cout << "y: " << msg.z() << std::endl;
}
