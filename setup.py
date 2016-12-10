#!/usr/bin/python

from setuptools import setup

install_requires = (
    'beautifulsoup4==4.5.1',
)

tests_require = (
    'nose',
)

setup_requires = (
    'flake8',
)

setup(
    name='tracking-id-injector',
    version='0.1.0',
    url='https://github.com/msufa/tracking-id-injector',
    author='Maciek Sufa',
    description=('Console script for injecting Google Analytics tracking IDs '
                 'into HTML files.'),
    license='Apache 2.0',
    packages=['tridinjector'],
    test_suite='nose.collector',
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=setup_requires,
    entry_points={
        'console_scripts': [
            'tracking-id-injector = tridinjector.injector:main'
        ]
    },
)
