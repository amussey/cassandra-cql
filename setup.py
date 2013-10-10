#!/usr/bin/env python

from distutils.core import setup

setup(
    name='cassandra-cql',
    version='1.0.0',
    description=('A tool for importing a *.cql3 file into a Cassandra database'),
    keywords='python cql cassandra',
    author='Andrew Mussey',
    author_email='admin@ajama.org',
    url='http://amussey.com',
    install_requires=["cql"],
    packages=['cassandra_cql'],
    scripts = [
        'scripts/cassandra-cql',
    ]
)
