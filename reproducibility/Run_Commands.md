# Reproducibility Commands

## Start the ROS Noetic container

From the Ubuntu host:

```bash
docker pull osrf/ros:noetic-desktop-full
docker start -ai lab2_ros1_noetic
```

Inside the container:

```bash
source /opt/ros/noetic/setup.bash
rosversion -d
```

Expected output:

```text
noetic
```

## Build the two-drone package

```bash
cd /root/vnav_ws
source /opt/ros/noetic/setup.bash
catkin build --force-cmake
source /root/vnav_ws/devel/setup.bash
```

## Run the two-drone scene

```bash
roslaunch two_drones_pkg two_drones.launch static:=True
roslaunch two_drones_pkg two_drones.launch
```

## Run the TurtleSim checks

```bash
roscore
rosrun turtlesim turtlesim_node
rosrun turtlesim turtle_teleop_key
rostopic echo /turtle1/cmd_vel
rosrun rqt_graph rqt_graph
```

## Run the TF tool checks

```bash
roslaunch turtle_tf turtle_tf_demo.launch
rosrun rqt_tf_tree rqt_tf_tree
rosrun tf tf_echo turtle1 turtle2
rviz
```

For the standard `turtle_tf` scripts, install the compatibility command before launching:

```bash
apt-get install -y python-is-python3
```
