# Copyright 2026 Inhatc
# Authors: Jeonggeun Lim

from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node
from rclpy.signals import SignalHandlerOptions
import time

class Controller(Node):
    def __init__(self):
        super().__init__('robowell_korea_agv_controller')
        self.init_parameters()
        self.init_publishers()
        self.timer_ = self.create_timer(self.control_period, self.controller_timer)
        self.cmd_vel = Twist()

    def init_parameters(self):
        self.declare_parameter('control.control_period', 0.1)
        self.control_period = self.get_parameter('control.control_period').value

    def init_publishers(self):
        self.cmd_vel_publisher_ = self.create_publisher(Twist, 'desired_cmd_vel', 10)

    def controller_timer(self):
        self.cmd_vel.linear.x = 0.1
        self.cmd_vel.angular.z = 0.0
        self.cmd_vel_publisher_.publish(self.cmd_vel)

    def stop(self):
        self.timer_.cancel()
        self.cmd_vel.linear.x = 0.0
        self.cmd_vel.angular.z = 0.0
        self.cmd_vel_publisher_.publish(self.cmd_vel)
        time.sleep(0.1)  # Ensure the stop command is sent before shutting down

def main(args=None):
    rclpy.init(args=args, signal_handler_options=SignalHandlerOptions.NO)

    robowell_korea_agv_controller = Controller()

    try:
        rclpy.spin(robowell_korea_agv_controller)
    except KeyboardInterrupt:
        pass
    finally:
        robowell_korea_agv_controller.stop()
        robowell_korea_agv_controller.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
