#!python
# coding=utf-8
from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


def version():
    with open('VERSION') as f:
        return f.read()


reqs = [line.strip() for line in open('requirements.txt')]

setup(
    name                = "thredds_iso_harvester",
    version             = version(),
    description         = "A Python library for generating ISO WAF folders from ncISO enabled THREDDS servers",
    long_description    = readme(),
    license             = 'MIT',
    author              = "Axiom Data Science",
    author_email        = "dev@axiomdatascience.com",
    url                 = "https://github.com/axiom-data-science/thredds_iso_harvester",
    packages            = find_packages(),
    install_requires    = reqs,
    classifiers         = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
    ],
    include_package_data = True,
    entry_points = {
        'console_scripts': [
            'thredds_iso_harvester=thredds_iso_harvester.cli:main'
        ]
    }
) 
