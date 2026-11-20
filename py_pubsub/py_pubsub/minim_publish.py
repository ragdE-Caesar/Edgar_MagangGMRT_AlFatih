import rclpy
from geometry_msgs.msg import Quaternion
from scipy.spatial.transform import Rotation as R
import math
from rclpy.node import Node

# from std_msgs.msg import Float64


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Quaternion, 'hidup_jokowi', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0.0

    def timer_callback(self):
        msg = Quaternion()
        msg.x = 0.0
        msg.y = 0.0
        msg.z = 0.717
        msg.w = 0.717
        self.publisher_.publish(msg)
        self.get_logger().info(f"{msg.x}, {msg.y}, {msg.z}, {msg.z}")
        #self.i += 30.0


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()