import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32
import math


class TrafficManager(Node):

    def __init__(self):
        super().__init__('traffic_manager')

        self.robot_pose = None
        self.robot_priority = None

        self.create_subscription(
            Pose2D,
            'robot_pose',
            self.pose_callback,
            10
        )

        self.create_subscription(
            Int32,
            'robot_priority',
            self.priority_callback,
            10
        )

    def pose_callback(self, msg):
        self.robot_pose = msg
        self.check_status()

    def priority_callback(self, msg):
        self.robot_priority = msg.data
        self.check_status()

    def check_status(self):

        if self.robot_pose is None or self.robot_priority is None:
            return

        my_x = 2.2
        my_y = 3.1
        my_priority = 1

        distance = math.sqrt(
            (self.robot_pose.x - my_x) ** 2 +
            (self.robot_pose.y - my_y) ** 2
        )

        safety_zone = 1.0

        if distance < safety_zone and self.robot_priority > my_priority:
            self.get_logger().warn('[DANGER] Yield to higher priority robot')

        else:
            self.get_logger().info('[CLEAR] Path is safe')


def main(args=None):
    rclpy.init(args=args)

    node = TrafficManager()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()