#ifndef PYBIND11_PROTOBUF_EXTRAS_HH
#define PYBIND11_PROTOBUF_EXTRAS_HH

#include "extras/msgs/vector3d.pb.h"

extras::msgs::Vector3d GetVector3d(double x, double y, double z);

void SetVector3d(const extras::msgs::Vector3d& msg);

#endif
