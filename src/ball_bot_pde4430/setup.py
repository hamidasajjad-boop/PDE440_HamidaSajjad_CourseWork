import os
from setuptools import find_packages, setup

package_name = 'ball_bot_pde4430'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),

        # package.xml
        ('share/' + package_name, ['package.xml']),

        # Launch files (NO spawn_gazebo.launch.py)
        (os.path.join('share', package_name, 'launch'),
            [
                'launch/bringup.launch.py',
                'launch/spawn_world.launch.py',
                'launch/spawn_robot.launch.py',
                'launch/view_robot.launch.py',
            ]),

        # World files
        (os.path.join('share', package_name, 'worlds'),
            ['worlds/default_world.sdf']),

        # URDF / XACRO / SDF
        (os.path.join('share', package_name, 'urdf'),
            [
                'urdf/ball_bot.xacro',
                'urdf/ball_bot.urdf',
                'urdf/ball_bot.sdf'
            ]),
    ],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hamida',
    maintainer_email='hamidasajjad65@gmail.com',
    description='Ball bot PDE4430 simulation project',
    license='MIT',

    entry_points={
        'console_scripts': [
            # Behavior node later
            'follow_ball = ball_bot_pde4430.follow_ball:main',
        ],
    },
)
