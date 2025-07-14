import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DroneController(Node):
    def __init__(self):
        super().__init__('drone_controller')
        self.publisher = self.create_publisher(Twist, '/drone1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.publish_cmd)

    def publish_cmd(self):
        msg = Twist()
        msg.linear.z = 0.5  # Constant upward thrust
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DroneController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

