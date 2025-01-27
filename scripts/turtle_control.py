#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Color

class TurtleControl():

   	# __init__(self) function is the class constructor.
    def __init__(self):
        self.pub = rospy.Publisher('cmd_vel',Twist,queue_size=1)
        self.rate = rospy.Rate(1) # 1hz
        # Set up command to publish
        self.cmd_vel = Twist()
        self.cmd_vel.linear.x = 0.5
        self.cmd_vel.angular.z = 0.5
        # Create a subscriber for color msg
        self.color = Color()
        rospy.Subscriber("color", Color, self.color_callback)

    # Callback for subscribed topic
    def color_callback(self,data):
        self.color = data

    def run(self):
        while not rospy.is_shutdown():
            # Publish our command!
            rospy.loginfo(f'The color I see is r={self.color.r} g={self.color.g} b={self.color.b}')
            self.pub.publish(self.cmd_vel)
            self.rate.sleep()

if __name__ == '__main__':
    rospy.init_node('turtle_control')
    # Invoke the run class function which does the actual work.
    try:
        ctrl = TurtleControl()
        ctrl.run()
    except rospy.ROSInterruptException:
        pass
