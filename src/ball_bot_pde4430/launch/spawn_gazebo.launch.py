from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
import xacro

def generate_launch_description():

    pkg_share = get_package_share_directory('ball_bot_pde4430')

    # World file
    world_path = os.path.join(pkg_share, 'worlds', 'default_world.sdf')

    # XACRO -> URDF on the fly
    xacro_file = os.path.join(pkg_share, 'urdf', 'ball_bot.xacro')
    robot_description = xacro.process_file(xacro_file).toxml()

    return LaunchDescription([

        # Launch Gazebo Harmonic with the world
        ExecuteProcess(
            cmd=['gz', 'sim', world_path],
            output='screen'
        ),

        # Robot state publisher (publishes TF + robot_description)
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
            output='screen'
        ),

        # Spawn robot into Gazebo using the robot_description topic
        ExecuteProcess(
            cmd=[
                'ros2', 'run', 'ros_gz_sim', 'create',
                '-name', 'ball_bot',
                '-topic', 'robot_description'
            ],
            output='screen'
        ),
    ])
