# Verified Experiment Code

This directory contains code used in the recorded experiments. It is intentionally separate from `report/`.

## Two-drone ROS package changes

`two_drones_pkg/src/frames_publisher_node.cpp` is the completed ROS1 TF publisher used for the successful catkin build.

`two_drones_pkg/src/plots_publisher_node_verified_change.cpp` records the verified TF2 lookup inserted into the supplied `plots_publisher_node.cpp` starter file.

The complete package checkout was executed inside the persistent Docker container at `/root/vnav_ws/src/two_drones_pkg` from upstream commit `609f31f`. The full package tree was not re-cloned on the Windows host because its GitHub connection was unavailable during packaging.

## TurtleSim controller

`turtlesim/turtle_motion_controller.py` publishes `geometry_msgs/Twist` messages to `/turtle1/cmd_vel` for 12 seconds and then publishes a zero command.
