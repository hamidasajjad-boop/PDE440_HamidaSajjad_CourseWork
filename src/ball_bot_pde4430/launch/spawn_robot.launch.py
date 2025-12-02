from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import xacro
import os

def generate_launch_description():

    pkg_share = get_package_share_directory('ball_bot_pde4430')

    xacro_file = os.path.join(pkg_share, 'urdf', 'ball_bot.xacro')
    robot_description = xacro.process_file(xacro_file).toxml()

    return LaunchDescription([

        # Publish robot_description + TF
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
            output='screen'
        ),

        # Spawn robot using ros_gz_sim
        ExecuteProcess(
            cmd=[
                'ros2', 'run', 'ros_gz_sim', 'create',
                '-name', 'ball_bot',
                '-topic', 'robot_description'
            ],
            output='screen'
        ),
    ])
