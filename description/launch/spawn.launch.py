#!/usr/bin/env python3
# Copyright 2026 Inhatc
# Authors: Jeonggeun Lim

import os
import tempfile

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    pkg_name = 'description'
    pkg_share = get_package_share_directory(pkg_name)

    urdf_path = os.path.join(pkg_share, 'urdf', 'rb_amr.urdf')

    with open(urdf_path, 'r') as f:
        urdf_xml = f.read()

    urdf_xml = urdf_xml.replace(
        f'package://{pkg_name}/',
        f'file://{pkg_share}/'
    )

    tmp_urdf = os.path.join(tempfile.gettempdir(), 'rb_amr_gazebo.urdf')
    with open(tmp_urdf, 'w') as f:
        f.write(urdf_xml)

    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            )
        )
    )

    spawn = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        output='screen',
        arguments=['-entity', 'rb_amr', '-file', tmp_urdf, '-z', '0.10']
    )

    return LaunchDescription([gazebo_launch, spawn])
