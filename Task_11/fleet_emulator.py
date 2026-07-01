import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32


class FleetEmulator(Node):

    def __init__(self):
        super().__init__('fleet_emulator')

        self.pose_pub = self.create_publisher(Pose2D, 'robot_pose', 10)
        self.priority_pub = self.create_publisher(Int32, 'robot_priority', 10)

        self.timer = self.create_timer(0.1, self.publish_data)

    def publish_data(self):

        pose = Pose2D()
        pose.x = 2.0
        pose.y = 3.0
        pose.theta = 0.0

        priority = Int32()
        priority.data = 0

        self.pose_pub.publish(pose)
        self.priority_pub.publish(priority)

        self.get_logger().info('Robot data published')


def main(args=None):
    rclpy.init(args=args)

    node = FleetEmulator()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()