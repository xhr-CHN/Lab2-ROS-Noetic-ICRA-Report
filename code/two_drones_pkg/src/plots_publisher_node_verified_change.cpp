// Verified Deliverable 3 change in plots_publisher_node.cpp.
// The surrounding class, tf2_ros::Buffer, and ref_frame/dest_frame variables
// are supplied by the MIT VNAV Lab2 starter package.

transform = parent->tf_buffer.lookupTransform(
    ref_frame,
    dest_frame,
    ros::Time(0));
