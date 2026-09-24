# Lab2 ROS Installation and TF Experiments

This package contains the final English report, verified source changes, experiment evidence, and reproducibility notes for Lab2.

## Final result

The recorded software-in-the-loop work completed:

- ROS1 Noetic access through an Ubuntu 20.04 Docker image on the Ubuntu 22.04 Lab1 virtual machine;
- catkin workspace initialization and ROS1 package compilation;
- TurtleSim startup, teleoperation, and Twist-based motion control;
- ROS nodes, topics, and rqt_graph inspection;
- turtle TF demo, rqt_tf_tree, tf_echo, and rViz TF display;
- two-drone TF broadcasting and relative-transform lookup;
- mathematical derivations, quaternion properties, and optional intrinsic/extrinsic rotation proof.

No physical UAV or robot was connected. The control experiment used TurtleSim as the permitted mobile-robot simulation equivalent.

## Directory guide

- `report/ICRA_LAB2_Report.pdf`: final submission PDF.
- `report/ICRA_LAB2_Report.tex`: LaTeX source.
- `report/ieeeconf.cls`: official IEEE/ICRA conference class used for compilation.
- `report/figures/`: all figures included in the report.
- `code/`: verified source changes and the TurtleSim controller used in the experiment.
- `source/`: source-version notes and upstream provenance.
- `evidence/`: original screenshot collection, extracted images, and later evidence images 18--26.
- `reproducibility/`: commands, completion matrix, and environment notes.

## Source provenance

The ROS package was executed from `MIT-SPARK/VNAV-labs` commit `609f31f`, the ROS1-compatible commit identified during the experiment. The repository tip was ROS2 `ament_cmake` and was intentionally not used for the successful catkin build.

The complete `two_drones_pkg` source snapshot is included under `code/two_drones_pkg/`, including `CMakeLists.txt`, `package.xml`, launch/configuration files, the mesh, and complete C++ source files.

Upstream repository: https://github.com/MIT-SPARK/VNAV-labs

## Known boundary

The course/Notion instructions describe Ubuntu 20.04 with native ROS Noetic. The verified setup used Ubuntu 22.04 as the host and `osrf/ros:noetic-desktop-full` as the container environment. This distinction is documented in the report.
