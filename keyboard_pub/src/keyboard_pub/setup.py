from setuptools import setup
import os
from glob import glob

package_name = 'keyboard_pub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # 包含 msg 文件夹中的自定义消息
        (os.path.join('share', package_name, 'msg'), glob('msg/*.msg'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': [
            'KeyboardStatePublisher = keyboard_pub.KeyboardStatePublisher:main',
    ],
},
) 