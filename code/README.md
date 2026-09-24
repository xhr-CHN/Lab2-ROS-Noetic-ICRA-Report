# Verified Experiment Code

This directory contains code used in the recorded experiments. It is intentionally separate from `report/`.

## Two-drone ROS package changes

`two_drones_pkg/` is the complete ROS1 package snapshot used for the successful catkin build. It includes `CMakeLists.txt`, `package.xml`, `launch/`, `config/`, `mesh/`, and `src/`.

`two_drones_pkg/src/frames_publisher_node.cpp` is the completed ROS1 TF publisher.

`two_drones_pkg/src/plots_publisher_node.cpp` is the complete relative-transform plotting node. `plots_publisher_node_verified_change.cpp` records the key lookup statement separately for auditability.

The package was executed inside the persistent Docker container at `/root/vnav_ws/src/two_drones_pkg` from upstream commit `609f31f`.

## TurtleSim controller

`turtlesim/turtle_motion_controller.py` publishes `geometry_msgs/Twist` messages to `/turtle1/cmd_vel` for 12 seconds and then publishes a zero command.
