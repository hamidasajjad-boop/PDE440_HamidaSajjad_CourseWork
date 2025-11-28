from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    pkg_share = get_package_share_directory('ball_bot_pde4430')
    urdf_path = os.path.join(pkg_share, 'urdf', 'ball_bot.urdf')

    with open(urdf_path, 'r') as file:
        robot_description_content = file.read()

    return LaunchDescription([

        # Joint State Publisher GUI (produces /joint_states)
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        ),

        # Robot State Publisher (publishes TF + robot_description)
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{
                'robot_description': robot_description_content
            }],
            output='screen'
        ),

        # RViz2 (visualizer)
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen'
        )
    ])
