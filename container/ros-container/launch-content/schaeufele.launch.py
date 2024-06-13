import os
import yaml

from launch import LaunchDescription
from launch_ros.actions import Node

from launch.substitutions import EnvironmentVariable, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    bento_drive = Node(
        package='bento_drive',
        executable='bento_drive_node',
        name='bento_drive_node',
        parameters=[ PathJoinSubstitution([ './', 'parameters', 'schaeufele.yaml' ]) ],
        namespace=EnvironmentVariable( 'EDU_ROBOT_NAMESPACE', default_value="bento" ),
        output='screen',
	emulate_tty=True,
    )

    camera_ros_1 = Node(
        package='camera_ros',
        executable='camera_node',
        name='camera_node_1',
        parameters=[ PathJoinSubstitution([ './', 'parameters', 'camera_ros_1.yaml' ]) ],
        namespace=PathJoinSubstitution([ EnvironmentVariable( 'EDU_ROBOT_NAMESPACE', default_value="bento" ), "cam1" ]),
        emulate_tty=True,
    )

    camera_ros_2 = Node(
        package='camera_ros',
        executable='camera_node',
        name='camera_node_2',
        parameters=[ PathJoinSubstitution([ './', 'parameters', 'camera_ros_2.yaml' ]) ],
        namespace=PathJoinSubstitution([ EnvironmentVariable( 'EDU_ROBOT_NAMESPACE', default_value="bento" ), "cam2" ]),
        emulate_tty=True,
    )

    return LaunchDescription([
        camera_ros_1,
#        camera_ros_2,
        bento_drive,
    ])
