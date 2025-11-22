import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # path to your URDF file
    urdf_path = os.path.join(
        os.getcwd(), 'urdf', 'push_bot.xacro'
    )

    spawn = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-file', urdf_path, '-entity', 'push_bot'],
        output='screen'
    )

    return LaunchDescription([spawn])
