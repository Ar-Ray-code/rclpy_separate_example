import launch
import launch_ros.actions

def generate_launch_description():

    hello = launch_ros.actions.Node(
        package="example_pkg_py", executable="scripts_main", output="screen",
    )

    return launch.LaunchDescription([
        hello
    ])