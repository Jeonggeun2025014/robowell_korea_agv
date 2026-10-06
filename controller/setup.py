# Copyright 2026 Inhatc
# Authors: Jeonggeun Lim

from setuptools import find_packages, setup
import os
import glob

package_name = 'controller'

setup(
    name=package_name,
    version='1.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/param', glob.glob(os.path.join('param', '*.yaml'))),
        ('share/' + package_name + '/launch', glob.glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jglim',
    maintainer_email='jglim@tinhatc.ac.kr',
    description='robowell korea agv controller',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robowell_korea_agv_controller = controller.controller:main',
            'robowell_korea_agv_robot = controller.robot:main',
            'robowell_korea_agv_arrow_teleop = controller.arrow_teleop:main',
        ],
    },
)
