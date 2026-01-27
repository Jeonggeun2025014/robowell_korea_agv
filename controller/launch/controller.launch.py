#!/usr/bin/env python3
# Copyright 2026 Inhatc
# Authors: Jeonggeun Lim

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    param_dir = LaunchConfiguration(
        'param_dir',
        default=os.path.join(
            get_package_share_directory('controller'),
            'param',
            'controller.yaml'
        )
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'param_dir',
            default_value=param_dir,
            description='Full path of parameter file'
        ),

        Node(
            package='controller',
            executable='robowell_korea_agv_controller',
            name='robowell_korea_agv_controller',
            parameters=[param_dir],   
            output='screen'
        ),

        Node(
            package='controller',
            executable='robowell_korea_agv_robot',
            name='robowell_korea_agv_robot',
            parameters=[param_dir],   
            output='screen'
        ),
    ])
