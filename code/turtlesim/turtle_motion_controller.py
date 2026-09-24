#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist


def main():
    rospy.init_node("turtle_motion_controller")
    publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(10)
    start_time = rospy.Time.now()
    duration = 12.0

    rospy.loginfo("Publishing Twist commands for %.1f seconds.", duration)

    while not rospy.is_shutdown():
        elapsed = (rospy.Time.now() - start_time).to_sec()
        if elapsed >= duration:
            break
        command = Twist()
        command.linear.x = 1.0
        command.angular.z = 0.6
        publisher.publish(command)
        rate.sleep()

    publisher.publish(Twist())
    rospy.loginfo("Motion command completed; robot stopped.")


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
