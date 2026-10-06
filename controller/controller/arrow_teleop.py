import sys
import termios
import tty

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


def get_key(settings):
    tty.setraw(sys.stdin.fileno())
    key = sys.stdin.read(1)
    if key == '\x1b':
        key += sys.stdin.read(2)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


class ArrowTeleop(Node):

    def __init__(self):
        super().__init__('arrow_teleop')
        self.pub = self.create_publisher(Twist, 'example_cmd_vel', 10)

        self.timer = self.create_timer(0.1, self.timer_callback)

        self.fixed_linear_speed = 0.1
        self.fixed_angular_speed = 0.1
        self.desired_cmd_vel = Twist()
        

    def timer_callback(self):
        self.desired_cmd_vel.linear.x = self.fixed_linear_speed
        self.desired_cmd_vel.angular.z = self.fixed_angular_speed
        
        self.pub.publish(self.desired_cmd_vel)  # Publish the desired command velocity


    def stop(self):
        twist = Twist()
        self.pub.publish(twist)


def main():
    settings = termios.tcgetattr(sys.stdin)

    rclpy.init()
    node = ArrowTeleop()

    print("\n시작")

    linear_x = 0.0
    angular_z = 0.0

    try:
        while rclpy.ok():
            key = get_key(settings)

            if key == '\x1b[A':
                linear_x = node.fixed_linear_speed
                angular_z = 0.0
            elif key == '\x1b[B':
                linear_x = -node.fixed_linear_speed
                angular_z = 0.0
            elif key == '\x1b[D':
                linear_x = node.fixed_linear_speed
                angular_z = node.fixed_angular_speed
            elif key == '\x1b[C':
                linear_x = node.fixed_linear_speed
                angular_z = -node.fixed_angular_speed
            elif key == ' ':
                linear_x = 0.0
                angular_z = 0.0
            elif key == 'q':
                break

            twist = Twist()
            twist.linear.x = linear_x
            twist.angular.z = angular_z
            node.pub.publish(twist)

    except Exception as e:
        print(e)

    finally:
        node.stop()
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        node.destroy_node()
        rclpy.shutdown()
        print("\n\n종료.")


if __name__ == '__main__':
    main()
    
    
