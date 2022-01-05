#ifndef PYBIND11_PROTOBUF_EXTRAS_HH
#define PYBIND11_PROTOBUF_EXTRAS_HH

#include "extras/msgs/pose.pb.h"
#include "extras/msgs/vector3d.pb.h"

extras::msgs::Vector3d MakeVector3d(double x, double y, double z);
void TakeVector3d(const extras::msgs::Vector3d& msg);

extras::msgs::Pose MakePose(double x, double y, double z);
void TakePose(const extras::msgs::Pose& msg);

#endif
