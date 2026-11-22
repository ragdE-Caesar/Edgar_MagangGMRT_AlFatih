import math
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray

PUBLISH_PERIOD = 1.0


class ArmPublisher(Node):

  def __init__(self):
    super().__init__('arm_publisher')
    self.arm_pub = self.create_publisher(
        Float64MultiArray, 'arm_controller/commands', 10
    )
    self.timer = self.create_timer(PUBLISH_PERIOD, self.publish_command)

    # Sudut input (radian)
    self.t1 = 0.0
    self.t2 = 0.0

  def calculate_fk(self, t1, t2):
    x = 2.0 * math.cos(t1) * math.cos(t2)
    y = 2.0 * math.cos(t2) * math.sin(t1)
    z = 2.0 - 2.0 * math.sin(t2)
    return x, y, z

  def publish_command(self):
    msg = Float64MultiArray()
    msg.data = [self.t1, self.t2, 0.0]
    self.arm_pub.publish(msg)

    x, y, z = self.calculate_fk(self.t1, self.t2)
    self.get_logger().info(f'{x:.5f}, {y:.5f}, {z:.5f}')


def main(args=None):
  rclpy.init(args=args)
  node = ArmPublisher()
  rclpy.spin(node)
  node.destroy_node()
  rclpy.shutdown()


if __name__ == '__main__':
  main()

