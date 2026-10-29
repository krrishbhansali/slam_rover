"""Publish the rover description and transforms from its joint states."""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import xacro


def generate_launch_description():
    pkg_share = get_package_share_directory('slam_rover')
    description = xacro.process_file(
        os.path.join(pkg_share, 'description', 'robot.urdf.xacro')).toxml()
    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='false'),
        Node(
            package='robot_state_publisher', executable='robot_state_publisher',
            output='screen', parameters=[{
                'robot_description': description,
                'use_sim_time': LaunchConfiguration('use_sim_time'),
            }]),
    ])
