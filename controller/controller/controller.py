
from geometry_msgs.msg import Twist 
import rclpy
from rclpy.node import Node

class Controller(Node):
    def __init__(self):
        super().__init__('robowell_korea_agv_controller')
        timer_period = 0.5  # seconds

        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

        self.timer = self.create_timer(timer_period, self.controller_timer)

    def controller_timer(self):
        msg = Twist()
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.angular.x)


def main(args=None):
    rclpy.init(args=args)

    robowell_korea_agv_controller = Controller()

    rclpy.spin(robowell_korea_agv_controller)

    robowell_korea_agv_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
