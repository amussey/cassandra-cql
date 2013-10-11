cassandra-cql
=============

`cassandra-cql` is a Python-based tool for importing CQL3 *.cql files into a Cassandra database (much in the same way you can use `mysql` to import *.sql files).

## Usage

`cassandra-cql` takes in the following parameters:

    cassandra-cql hostname port cql_file [-f]

So, for example, it can be executed by running:

    cassandra-cql localhost 9160 /path/to/cql_file.cql

By default, this script will stop if it hits an error with any of the commands in the file.  This functionality can be overwritten using the -f flag.

    cassandra-cql localhost 9160 /path/to/cql_file.cql -f


## Installation

This package is currently installable directly from the git repo:

    pip install -e git+https://github.com/amussey/cassandra-cql#egg=cassandra-cql
