from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import xacro
import os

def generate_launch_description():

    pkg = get_package_share_directory('ball_bot_pde4430')

    # WORLD
    world_path = os.path.join(pkg, 'worlds', 'default_world.sdf')

    # Load Xacro robot
    xacro_file = os.path.join(pkg, 'urdf', 'ball_bot.xacro')
    robot_description = xacro.process_file(xacro_file).toxml()

    return LaunchDescription([

        # 1) Launch Gazebo with OGRE renderer
        ExecuteProcess(
            cmd=[
                'gz', 'sim',
                '--render-engine', 'ogre',   # <<< FIX: use OGRE renderer
                '-v', '4',
                world_path
            ],
            output='screen'
        ),

        # 2) Publish TF + robot_description
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
            output='screen'
        ),

        # 3) Spawn robot
        ExecuteProcess(
            cmd=[
                'ros2', 'run', 'ros_gz_sim', 'create',
                '-name', 'ball_bot',
                '-topic', 'robot_description',
                '-z', '0.05'
            ],
            output='screen'
        ),
    ])
