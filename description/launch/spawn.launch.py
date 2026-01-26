# #!/usr/bin/env python3
# import os
# from ament_index_python.packages import get_package_share_directory
# from launch import LaunchDescription
# from launch_ros.actions import Node

# def generate_launch_description():
#     pkg = get_package_share_directory('description')
#     urdf_path = os.path.join(pkg, 'urdf', 'rb_amr.urdf')

#     gazebo = Node(
#         package='gazebo_ros',
#         executable='gazebo',
#         output='screen',
#         arguments=['-s', 'libgazebo_ros_factory.so']
#     )

#     spawn = Node(
#         package='gazebo_ros',
#         executable='spawn_entity.py',
#         output='screen',
#         arguments=['-entity', 'rb_amr', '-file', urdf_path, '-z', '0.10']
#     )

#     return LaunchDescription([gazebo, spawn])


# #!/usr/bin/env python3
# import os
# import tempfile

# from ament_index_python.packages import get_package_share_directory
# from launch import LaunchDescription
# from launch.actions import IncludeLaunchDescription
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch_ros.actions import Node


# def generate_launch_description():
#     pkg = get_package_share_directory('description')  # 패키지명에 맞게
#     urdf_path = os.path.join(pkg, 'urdf', 'rb_amr.urdf')

#     gazebo_launch = IncludeLaunchDescription(
#         PythonLaunchDescriptionSource(
#             os.path.join(
#                 get_package_share_directory('gazebo_ros'),
#                 'launch',
#                 'gazebo.launch.py'
#             )
#         )
#     )

#     spawn = Node(
#         package='gazebo_ros',
#         executable='spawn_entity.py',
#         output='screen',
#         arguments=['-entity', 'rb_amr', '-file', urdf_path, '-z', '0.10']
#     )

#     return LaunchDescription([gazebo_launch, spawn])

#!/usr/bin/env python3
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

    # 원본 URDF
    urdf_path = os.path.join(pkg_share, 'urdf', 'rb_amr.urdf')

    # URDF 읽고 package:// 경로를 file:// 절대경로로 바꿈
    with open(urdf_path, 'r') as f:
        urdf_xml = f.read()

    urdf_xml = urdf_xml.replace(
        f'package://{pkg_name}/',
        f'file://{pkg_share}/'
    )

    # 임시 URDF 파일로 저장 후 spawn
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
