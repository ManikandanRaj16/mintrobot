#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TwistStamped


class TwistToTwistStamped(Node):
    """Converts Twist messages to TwistStamped messages"""
    
    def __init__(self):
        super().__init__('twist_to_twist_stamped')
        
        # Subscribe to Twist messages from keyboard teleop
        self.subscription = self.create_subscription(
            Twist,
            '/mintrobot_controller/cmd_vel_twist',
            self.twist_callback,
            10
        )
        
        # Publish TwistStamped messages to controller
        self.publisher = self.create_publisher(
            TwistStamped,
            '/mintrobot_controller/cmd_vel',
            10
        )
        
        self.get_logger().info('Twist to TwistStamped converter started')
        self.get_logger().info('Subscribing to: /mintrobot_controller/cmd_vel_twist (Twist)')
        self.get_logger().info('Publishing to: /mintrobot_controller/cmd_vel (TwistStamped)')
    
    def twist_callback(self, msg):
        """Convert Twist to TwistStamped"""
        twist_stamped = TwistStamped()
        twist_stamped.header.stamp = self.get_clock().now().to_msg()
        twist_stamped.header.frame_id = 'base_footprint'
        twist_stamped.twist = msg
        self.publisher.publish(twist_stamped)


def main(args=None):
    rclpy.init(args=args)
    node = TwistToTwistStamped()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()

