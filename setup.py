"""A setuptools for installing the Slurm Account Usage Reporter.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='slurm_usage_reporter',

    version='1.0.0',

    description='A SLURM usage reporting and analysis tool written in Python 3 by Ravindra Shinde',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/neelravi/slurm_usage_reporter',

    # Author details
    author='Ravindra Shinde',
    author_email='neelravi@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',


        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
       'Programming Language :: Python :: 3.5',
    ],

    # What is your project about?
    keywords='SLURM accounting usage report analysis',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['numpy'],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    entry_points={
        'console_scripts': [
            'slurm_usage_reporter=slurm_usage_reporter:main',
        ],
    },
)
