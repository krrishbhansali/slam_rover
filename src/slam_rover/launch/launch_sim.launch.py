"""Spawn Slam Rover in Gazebo Classic, including simulated lidar and camera."""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    pkg_share = get_package_share_directory('slam_rover')
    return LaunchDescription([
        DeclareLaunchArgument(
            'world', default_value=os.path.join(pkg_share, 'worlds', 'obstacles.world'),
            description='Absolute path to a Gazebo Classic world file'),
        DeclareLaunchArgument('gui', default_value='true'),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(pkg_share, 'launch', 'rsp.launch.py')),
            launch_arguments={'use_sim_time': 'true'}.items()),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(
                get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')),
            launch_arguments={
                'world': LaunchConfiguration('world'),
                'gui': LaunchConfiguration('gui'),
            }.items()),
        Node(
            package='gazebo_ros', executable='spawn_entity.py', output='screen',
            arguments=['-topic', 'robot_description', '-entity', 'slam_rover'],
            parameters=[{'use_sim_time': True}]),
    ])
