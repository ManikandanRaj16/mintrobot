from setuptools import setup

package_name = 'mintrobot_py_examples'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='antonio.brandi@outlook.it',
    description='ROS 2 Code Examples',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_publisher = mintrobot_py_examples.simple_publisher:main',
            'simple_subscriber = mintrobot_py_examples.simple_subscriber:main',
            'simple_parameter = mintrobot_py_examples.simple_parameter:main',
            'simple_turtlesim_kinematics = mintrobot_py_examples.simple_turtlesim_kinematics:main',
            'simple_service_server = mintrobot_py_examples.simple_service_server:main',
            'simple_service_client = mintrobot_py_examples.simple_service_client:main',
            'simple_tf_kinematics = mintrobot_py_examples.simple_tf_kinematics:main',
        ],
    },
)