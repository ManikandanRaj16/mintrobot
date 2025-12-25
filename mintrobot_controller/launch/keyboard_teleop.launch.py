"""
Keyboard Teleop Launch File

NOTE: teleop_twist_keyboard requires an interactive terminal (stdin) and cannot be 
run via a launch file. Use one of these options instead:

Option 1 - Run directly:
  ros2 run teleop_twist_keyboard teleop_twist_keyboard \
    --ros-args --remap cmd_vel:=/mintrobot_controller/cmd_vel

Option 2 - Use the provided script:
  ./src/mintrobot_controller/scripts/keyboard_teleop.sh
"""

from launch import LaunchDescription
from launch.actions import LogInfo


def generate_launch_description():
    """
    Keyboard teleop cannot be launched via launch file due to terminal requirements.
    This file exists for documentation only.
    """
    
    info_message = LogInfo(
        msg="\n"
            "========================================\n"
            "Keyboard teleop requires an interactive terminal.\n"
            "Run this command directly:\n"
            "  ros2 run teleop_twist_keyboard teleop_twist_keyboard \\\n"
            "    --ros-args --remap cmd_vel:=/mintrobot_controller/cmd_vel\n"
            "\n"
            "Or use the script:\n"
            "  ./src/mintrobot_controller/scripts/keyboard_teleop.sh\n"
            "========================================\n"
    )

    return LaunchDescription([info_message])

