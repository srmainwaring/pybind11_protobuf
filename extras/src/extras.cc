#include "extras.hh"

extras::msgs::Vector3d MakeVector3d(double x, double y, double z)
{
  extras::msgs::Vector3d msg;
  msg.set_x(x);
  msg.set_y(y);
  msg.set_z(z);
  return msg;
}

void TakeVector3d(const extras::msgs::Vector3d& msg)
{
  std::cout << msg.DebugString();
}

extras::msgs::Pose MakePose(double x, double y, double z)
{
  extras::msgs::Vector3d pos;
  pos.set_x(x);
  pos.set_y(y);
  pos.set_z(z);

  extras::msgs::Pose msg;
  *msg.mutable_position() = pos;

  return msg;
}

void TakePose(const extras::msgs::Pose& msg)
{
  std::cout << msg.DebugString();
}
