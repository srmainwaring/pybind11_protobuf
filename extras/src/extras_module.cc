#include <pybind11/pybind11.h>

#include "pybind11_protobuf/native_proto_caster.h"

#include "extras.hh"

namespace py = pybind11;

PYBIND11_MODULE(extras_module, m) {
  pybind11_protobuf::ImportNativeProtoCasters();

  m.def("make_vector3d", &MakeVector3d,
      pybind11::arg("x"),
      pybind11::arg("y"),
      pybind11::arg("z"));
  
  m.def("take_vector3d", &TakeVector3d,
      pybind11::arg("msg"));

  m.def("make_pose", &MakePose,
      pybind11::arg("x"),
      pybind11::arg("y"),
      pybind11::arg("z"));
  
  m.def("take_pose", &TakePose,
      pybind11::arg("msg"));
}
