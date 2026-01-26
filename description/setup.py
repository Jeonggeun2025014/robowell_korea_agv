import os
from glob import glob
from setuptools import setup

package_name = 'description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        # 패키지 인덱스 등록
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        # package.xml 설치
        ('share/' + package_name, ['package.xml']),

        # ✅ 아래 3줄이 없으면 launch/urdf/meshes가 install에 안 들어갑니다
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='you@example.com',
    description='Robot description with STL/URDF and launch files',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={'console_scripts': []},
)
