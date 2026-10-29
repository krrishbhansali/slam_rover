"""Start an optional physical USB camera; Gazebo supplies its own camera."""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('video_device', default_value='/dev/video0'),
        Node(
            package='v4l2_camera', executable='v4l2_camera_node', output='screen',
            parameters=[{
                'video_device': LaunchConfiguration('video_device'),
                'image_size': [640, 480],
                'camera_frame_id': 'camera_link_optical',
            }]),
    ])
