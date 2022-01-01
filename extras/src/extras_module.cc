#include <pybind11/pybind11.h>

#include "google/protobuf/message.h"
#include "pybind11_protobuf/native_proto_caster.h"
#include "extras/msgs/vector3d.pb.h"
#include "extras.hh"

namespace py = pybind11;

PYBIND11_MODULE(extras_module, m) {
  pybind11_protobuf::ImportNativeProtoCasters();

  m.def("get_vector3d", &GetVector3d,
      pybind11::arg("x"),
      pybind11::arg("y"),
      pybind11::arg("z"));
  
  m.def("set_vector3d", &SetVector3d,
      pybind11::arg("msg"));
}
