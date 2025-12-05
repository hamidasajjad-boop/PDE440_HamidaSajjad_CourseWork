from launch import LaunchDescription
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    pkg_share = get_package_share_directory('ball_bot_pde4430')
    world_path = os.path.join(pkg_share, 'worlds', 'default_world.sdf')

    return LaunchDescription([
        ExecuteProcess(
            cmd=[
                'gz', 'sim',
                '--render-engine', 'ogre',    # <<< FIX: FORCE OGRE RENDERER
                world_path
            ],
            output='screen'
        )
    ])
