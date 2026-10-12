# Copyright 2026 Inhatc
# Authors: Jeonggeun Lim

from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
import rclpy
from rclpy.node import Node

class Robot(Node):
    def __init__(self):
        super().__init__('robowell_korea_agv_robot')
        self.init_variables()
        self.init_parameters()
        self.init_subscribers()

    def init_variables(self):
        self.agv_pose = Pose()

    def init_parameters(self):
        self.declare_parameter('robot.wheels.seperation', 0.160)
        self.declare_parameter('robot.wheels.radius', 0.033)
        self.wheel_seperation = self.get_parameter('robot.wheels.seperation').value
        self.wheel_radius = self.get_parameter('robot.wheels.radius').value

    def init_subscribers(self):
        self.subscriber_ = self.create_subscription(
            Twist, 'desired_cmd_vel', self.subscribe_cmd_vel, 10)

    def subscribe_cmd_vel(self, msg: Twist):
        self.calculate_motor_rpm(msg)

    def calculate_motor_rpm(self, msg: Twist):
        self.get_logger().info(f'cmd_vel: lin.x={msg.linear.x}, ang.z={msg.angular.z}')
        # Insert function to calculate motor rpm from cmd_vel
        # and 
        # Send rpm to motor controller

def main(args=None):
    rclpy.init(args=args)

    robowell_korea_agv_robot = Robot()

    try:
        rclpy.spin(robowell_korea_agv_robot)
    except KeyboardInterrupt:
        pass
    finally:
        robowell_korea_agv_robot.destroy_node()
        rclpy.try_shutdown()

if __name__ == '__main__':
    main()
