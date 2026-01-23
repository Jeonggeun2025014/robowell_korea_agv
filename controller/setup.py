from setuptools import find_packages, setup

package_name = 'controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'robowell_korea_agv_robot = controller.robot:main'
        ],
    },
)
