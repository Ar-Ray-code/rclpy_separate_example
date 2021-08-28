from setuptools import setup, find_packages
import glob
import os

package_name = 'example_pkg_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/data.launch.py']),
        # (os.path.join('share', package_name), glob('./launch/*.launch.py')),

    ],

    entry_points={
        'console_scripts': [
            'scripts_main = '+ package_name +'.scripts_main:ros_main',
        ],
    }
)