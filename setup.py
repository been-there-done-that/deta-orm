#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="__Deesh__",
    author_email='internetwasmyidea@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="a orm like interactive wrapper for deta base.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='deta_orm',
    name='deta_orm',
    packages=find_packages(include=['deta_orm', 'deta_orm.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/been-there-done-that/deta_orm',
    version='0.1.0',
    zip_safe=False,
)
