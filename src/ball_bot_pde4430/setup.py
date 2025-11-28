import os
from setuptools import find_packages, setup

package_name = 'ball_bot_pde4430'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    
    data_files=[
        # ROS package index
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),

        # Package.xml
        ('share/' + package_name, ['package.xml']),

        # Install URDF
        (os.path.join('share', package_name, 'urdf'),
            ['urdf/ball_bot.urdf',
  'urdf/robot_view.rviz']),

        # Install Launch files
        (os.path.join('share', package_name, 'launch'),
            [
                'launch/gazebo_robot.launch.py',
                'launch/view_robot.launch.py'
            ]),

        # Install Worlds folder (empty for now)
        (os.path.join('share', package_name, 'worlds'), []),

        # Install Config folder (empty for now)
        (os.path.join('share', package_name, 'config'), []),
    ],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hamida',
    maintainer_email='hamidasajjad65@gmail.com',
    description='Ball bot PDE4430 project',
    license='TODO: License declaration',

    extras_require={'test': ['pytest']},

    entry_points={
        'console_scripts': [
            # We will add nodes later
        ],
    },
)
