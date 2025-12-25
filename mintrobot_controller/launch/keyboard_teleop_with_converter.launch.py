from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    """
    Launch file for keyboard teleop with Twist to TwistStamped converter.
    
    NOTE: The keyboard teleop itself must be run separately in a terminal:
    ros2 run teleop_twist_keyboard teleop_twist_keyboard \
      --ros-args --remap cmd_vel:=/mintrobot_controller/cmd_vel_twist
    
    Or use the script:
    ./src/mintrobot_controller/scripts/keyboard_teleop.sh
    """

    # Converter node: converts Twist to TwistStamped
    twist_converter = Node(
        package="mintrobot_controller",
        executable="twist_to_twist_stamped.py",
        name="twist_to_twist_stamped",
        output="screen"
    )

    return LaunchDescription([twist_converter])

