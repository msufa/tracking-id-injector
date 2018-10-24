from setuptools import setup

install_requires = (
    'beautifulsoup4==4.6.3',
)

tests_require = (
    'pytest',
    'pytest-cov',
    'mock',
)

setup_requires = (
    'pytest-runner',
    'flake8',
)

setup(
    name='tracking-id-injector',
    version='1.0.1',
    url='https://github.com/msufa/tracking-id-injector',
    author='Maciek Sufa',
    description=('Console script for injecting Google Analytics tracking IDs '
                 'into HTML files.'),
    license='Apache 2.0',
    packages=['tridinjector'],
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=setup_requires,
    entry_points={
        'console_scripts': [
            'tracking-id-injector = tridinjector.injector:main'
        ]
    },
)
