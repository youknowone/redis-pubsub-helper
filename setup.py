from __future__ import with_statement

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version():
    with open('redispubsub/version.txt') as f:
        return f.read().strip()


def get_readme():
    try:
        with open('README.rst') as f:
            return f.read().strip()
    except IOError:
        return ''

setup(
    name='redis-pubsub-helper',
    version=get_version(),
    description='Redis pubsub non-blocking interface (With a thread).',
    long_description=get_readme(),
    author='Jeong YunWon',
    author_email='jeong+redispubsub@youknowone.org',
    url='https://github.com/youknowone/redis-pubsub',
    packages=(
        'redispubsub',
    ),
    package_data={
        'redispubsub': ['version.txt']
    },
    install_requires=[
        'distribute',
        'redis',
    ],
)