import os
from setuptools import find_packages, setup

package_name = 'ball_bot_pde4430'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            [
                'launch/spawn_gazebo.launch.py',
                'launch/view_robot.launch.py'
            ]),
        (os.path.join('share', package_name, 'worlds'),
            ['worlds/default_world.sdf']),
        (os.path.join('share', package_name, 'urdf'),
            ['urdf/ball_bot.xacro']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hamida',
    maintainer_email='hamidasajjad65@gmail.com',
    description='Ball bot PDE4430 project',
    license='TODO',
    entry_points={'console_scripts': []},
)
