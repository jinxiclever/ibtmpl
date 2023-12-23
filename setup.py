#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="ibtmpl",
    author_email='yu.zheng@inboc.net',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    entry_points={
        'console_scripts': [
            'ibtmpl=ibtmpl.main:run_tool',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='ibtmpl',
    name='ibtmpl',
    packages=find_packages(include=['ibtmpl', 'ibtmpl.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/zhengyu-inboc/ibtmpl',
    version='0.2.2dev0',
    zip_safe=False,
    package_data={'': ['*.yaml']},
)
