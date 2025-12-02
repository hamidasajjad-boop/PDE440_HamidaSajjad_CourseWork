from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import xacro
import os

def generate_launch_description():

    pkg_share = get_package_share_directory('ball_bot_pde4430')
    xacro_path = os.path.join(pkg_share, 'urdf', 'ball_bot.xacro')

    robot_description = xacro.process_file(xacro_path).toxml()

    return LaunchDescription([
        
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}]
        ),

        Node(
            package='rviz2',
            executable='rviz2'
        )
    ])
