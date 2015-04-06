#! /usr/bin/env python
import sys
from setuptools import setup, find_packages
from thredds_iso_harvester import __version__

def readme():
    with open('README.md') as f:
        return f.read()

reqs = [line.strip() for line in open('requirements.txt')]

setup(
    name                = "thredds_iso_harvester",
    version             = __version__,
    description         = "A Python library for generating ISO WAF folders from THREDDS servers",
    long_description    = readme(),
    license             = 'GPLv3',
    author              = "Axiom Data Science",
    author_email        = "dev@axiomdatascience.com",
    url                 = "https://github.com/axiom-data-science/thredds_iso_harvester",
    packages            = find_packages(),
    install_requires    = reqs,
    #tests_require       = ['pytest'],
    #cmdclass            = {'test': PyTest},
    classifiers         = [
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering',
        ],
    include_package_data = True,
) 
