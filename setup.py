from setuptools import setup
# For launch files
import os
from glob import glob

package_name = 'rps_turtle_control'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files
        (os.path.join('share', package_name, 'launch'),
         glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Damjan',
    maintainer_email='damjan@romb-technologies.hr',
    description='Simple turtlesim control for RPS class examples.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle_control = rps_turtle_control.turtle_control:main'
        ],
    },
)
