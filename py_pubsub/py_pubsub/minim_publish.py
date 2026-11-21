from geometry_msgs.msg import Quaternion

import rclpy
from rclpy.node import Node


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Quaternion, 'hidup_jokowi', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Quaternion()
        msg.x = 0.0
        msg.y = 0.0
        msg.z = 0.5
        msg.w = 1.0
        self.publisher_.publish(msg)
        self.get_logger().info(
            f'Published quaternion: x={msg.x}, y={msg.y}, '
            f'z={msg.z}, w={msg.w}')


def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
