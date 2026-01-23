from geometry_msgs.msg import Twist 
from geometry_msgs.msg import PoseArray
from geometry_msgs.msg import Pose
import rclpy
from rclpy.node import Node

class Robot(Node):
    def __init__(self):
        super().__init__('robowell_korea_agv_robot')

        # init_variable()
        # init_subscriber()

    def init_variable(self):
        self.agv_pose = Pose()

    def init_subscriber(self):
        self.subscriber_ = self.create_subscription(Twist, 'cmd_vel', self.cmd_vel_callback, 10)

    def cmd_vel_callback(self, msg:Twist):
        self.get_logger().info('Subscribing: "%s"' % msg.angular.x)


def main(args=None):
    rclpy.init(args=args)

    robowell_korea_agv_robot = Robot()

    rclpy.spin(robowell_korea_agv_robot)

    robowell_korea_agv_robot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
