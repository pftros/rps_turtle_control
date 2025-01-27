#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from turtlesim.msg import Color

class TurtleControl(Node):

   	# __init__(self) function is the class constructor.
    def __init__(self):
        super().__init__('turtle_control')
        self.pub = self.create_publisher(Twist,'cmd_vel',1)
        self.timer = self.create_timer(1, self.timer_callback) # 1hz
        # Set up command to publish
        self.cmd_vel = Twist()
        self.cmd_vel.linear.x = 0.5
        self.cmd_vel.angular.z = 0.5
        # Create a subscriber for color msg
        self.color = Color()
        self.sub = self.create_subscription(Color,'color',self.color_callback,1)

    # Callback for subscribed topic
    def color_callback(self,data):
        self.color = data

    def timer_callback(self):
        # Publish our command!
        self.get_logger().info(f'The color I see is r={self.color.r} g={self.color.g} b={self.color.b}')
        self.pub.publish(self.cmd_vel)

def main(args=None):
    rclpy.init(args=args)
    ctrl = TurtleControl()
    rclpy.spin(ctrl)

    # Explicit destruction (optional)
    ctrl.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
