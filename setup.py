"""
setup
~~~~~

:copyright: (c) 2013-2014 by Linovia, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from setuptools import setup, find_packages
import sys


with open('requirements.txt') as f:
    install_requires = f.read()


setup(
    name='django-agile-boards',
    version='0.1.1',
    author='Xavier Ordoquy',
    author_email='xordoquy@linovia.com',
    url='https://www.linovia.com',
    description='Agile boards web application.',
    long_description=open('README.md').read(),
    packages=find_packages('.'),
    zip_safe=False,
    install_requires=install_requires,
    license='BSD',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'agileboards = agileboards.runner:main',
        ],
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
