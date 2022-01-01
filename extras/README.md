# pybind11_protobuf - extra examples

This directory contains some additional examples that use pybind11_protobuf

## Install

Run the install script:

```bash
$ ./scripts/build_and_run_tests.sh
```

## Usage

The examples should be run inside the virtual environment created by the install script.

```bash
$ source ./venv/bin/activate
```

Build

```bash
(venv) bazel build //extras/python:extras_example
```

Run

```bash
(venv) ./bazel-bin/extras/python/extras_example

Extras Module Example
===================

cpp vector3d
------------
x: 1.0
y: 2.0
z: 3.0

isinstance: True

Set Vector3d
------------
x: 1
y: 2
y: 3

py vector3d
-----------
x: 53.1
y: 23.7
z: 10.2

isinstance: True

Set Vector3d
------------
x: 53.1
y: 23.7
y: 10.2
```


## Issues

The example does not work correctly when using the C++ implementation.

```bash
(venv) bazel clean
(venv) export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=cpp
(venv) bazel build //extras/python:extras_example
...
(venv) ./bazel-bin/extras/python/extras_example

Extras Module Example
===================

google.protobuf implementation
------------------------------
cpp

cpp vector3d
------------
x: 1.0
y: 2.0
z: 3.0

isinstance: False

Traceback (most recent call last):
  File "/Volumes/MacPro2_DV1/Code/python/pybind11_protobuf/./bazel-bin/extras/python/extras_example.runfiles/com_google_pybind11_protobuf/extras/python/extras_example.py", line 44, in <module>
    main()
  File "/Volumes/MacPro2_DV1/Code/python/pybind11_protobuf/./bazel-bin/extras/python/extras_example.runfiles/com_google_pybind11_protobuf/extras/python/extras_example.py", line 29, in main
    msg = m.set_vector3d(msg)
TypeError: set_vector3d(): incompatible function arguments. The following argument types are supported:
    1. (msg: extras::msgs::Vector3d) -> None

Invoked with: x: 1.0
y: 2.0
z: 3.0
```
