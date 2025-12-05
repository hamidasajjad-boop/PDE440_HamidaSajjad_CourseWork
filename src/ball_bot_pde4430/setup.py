from setuptools import setup
import os
from glob import glob

package_name = 'ball_bot_pde4430'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        # Install launch files
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),

        # Install XACRO only, not URDF
        (os.path.join('share', package_name, 'urdf'),
            glob('urdf/*.xacro')),

        # worlds
        (os.path.join('share', package_name, 'worlds'),
            glob('worlds/*.sdf')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hamida',
    maintainer_email='hamidasajjad65@gmail.com',
    description='Ball Bot PDE4430 project',
    license='MIT',
    entry_points={
        'console_scripts': [],
    },
)
