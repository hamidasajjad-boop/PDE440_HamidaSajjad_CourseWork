from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    pkg_path = get_package_share_directory('ball_bot_pde4430')

    urdf_path = os.path.join(pkg_path, 'urdf', 'ball_bot.urdf')
    with open(urdf_path, 'r') as f:
        robot_desc = f.read()

    world_path = os.path.join(pkg_path, 'worlds', 'assessment_world.world')

    return LaunchDescription([

        # 1. Launch IGNITION GAZEBO (HARMONIC)
        ExecuteProcess(
            cmd=[
                'gz', 'sim', '-v', '4', world_path
            ],
            output='screen'
        ),

        # 2. Publish TF + robot_description
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': robot_desc
            }]
        ),

        # 3. Spawn robot inside Gazebo (Ignition)
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=[
                '-string', robot_desc,
                '-name', 'ball_bot',
                '-allow_renaming', 'true'
            ],
            output='screen'
        ),

        # 4. Start RViz2 (optional)
        Node(
            package='rviz2',
            executable='rviz2',
            output='screen'
        ),
    ])
