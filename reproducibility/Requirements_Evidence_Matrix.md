# Requirements and Evidence Matrix

| Requirement | Verified operation | Evidence |
|---|---|---|
| ROS Noetic environment | Docker image, `rosversion -d`, catkin workspace | `20_rosdep_update_success.png`, report figures 1--4 |
| TurtleSim and teleoperation | `turtlesim_node`, `turtle_teleop_key` | `18_turtlesim_teleop_motion.png` |
| Twist topic | `rostopic echo /turtle1/cmd_vel` | `21_turtle_cmd_vel_echo.png` |
| TurtleSim ROS graph | `rqt_graph` | `22_turtlesim_rqt_graph.png` |
| Turtle TF demo | `roslaunch turtle_tf turtle_tf_demo.launch` | `23_turtle_tf_demo.png` |
| TF tree | `rqt_tf_tree` | `24_rqt_tf_tree.png` |
| Numerical TF query | `tf_echo turtle1 turtle2` | `25_tf_echo_turtle1_turtle2.png` |
| rViz TF display | Fixed frame `world`, TF display enabled | `26_rviz_tf_display.png` |
| Two-drone TF experiment | Static/dynamic launch, TF publisher, TF lookup | Evidence 01--16 and report figures |
| Mathematical tasks | Parabola, relative position, plane, ellipse, quaternions | Report Sections IV--V |
| Optional rotation task | Intrinsic/extrinsic matrix proof | Report Section IV |

## Limitations

The evidence proves ROS simulation and visualization. It does not prove physical UAV execution, hardware timing, or native Ubuntu 20.04 installation outside Docker.
