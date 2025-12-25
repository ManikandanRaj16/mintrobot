#!/bin/bash

# Keyboard teleop for mintrobot controller
# This script runs teleop_twist_keyboard with the correct remapping

# Source ROS 2 setup if not already sourced
if [ -z "$ROS_DISTRO" ]; then
    if [ -f /opt/ros/humble/setup.bash ]; then
        source /opt/ros/humble/setup.bash
    else
        echo "Error: ROS 2 setup file not found at /opt/ros/humble/setup.bash"
        exit 1
    fi
fi

# Source workspace if it exists (try both old and new workspace names)
if [ -f ~/bumperbot_ws/install/setup.bash ]; then
    source ~/bumperbot_ws/install/setup.bash
elif [ -f ~/mintrobot_ws/install/setup.bash ]; then
    source ~/mintrobot_ws/install/setup.bash
fi

# Check if running in interactive terminal
if [ ! -t 0 ]; then
    echo "Error: This script requires an interactive terminal."
    echo "Please run it directly in your terminal, not via a launch file or non-interactive script."
    exit 1
fi

# Run keyboard teleop with remapping to a temp topic
# The converter node will convert Twist to TwistStamped
exec ros2 run teleop_twist_keyboard teleop_twist_keyboard \
  --ros-args --remap cmd_vel:=/mintrobot_controller/cmd_vel_twist

