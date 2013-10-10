#! /usr/bin/env python
'''
This file is used to inject a full *.cql file into a Cassandra database.
To run this script, all three command line parameters are required:
    
    python cassandra-cql.py hostname port script_file

An example script file would be:

    USE keyspace;

    CREATE COLUMNFAMILY projects (
      KEY uuid PRIMARY KEY,
      project_id int,
      name text
    );

'''
import cql
import sys
from cassandra_cql.bcolors import bcolors

def cql_execute(host, port, filename, force):
    connection = cql.connect(host=host, port=port, cql_version='3.0.0')
    cursor = connection.cursor()

    cql_file = open(filename)
    cql_command_list = ''.join(cql_file.readlines()).split(";")

    for cql_command in cql_command_list:
        if cql_command.replace('\n', ''):
            print '\n{command}'.format(command=cql_command.strip('\n'))

            try:
                cursor.execute('{command};'.format(command=cql_command.replace('\n', ' ')))
                print '{color_start}Success!{color_end}'.format(error=e, color_start=bcolors.OKGREEN, color_end=bcolors.ENDC)
            except cql.ProgrammingError as e:
                print '{color_start}{error}{color_end}'.format(error=e, color_start=bcolors.FAIL, color_end=bcolors.ENDC)
                if not force:
                    print '\n{color_start}Execution of script {filename} failed!\nSee the error message above for details.{color_end}'.format(color_start=bcolors.FAIL,
                                                                                                    color_end=bcolors.ENDC,
                                                                                                    filename=filename)
                    sys.exit(-1)
    print '\n{color_start}Execution of script {filename} complete!{color_end}'.format(color_start=bcolors.OKBLUE,
                                                                                      color_end=bcolors.ENDC,
                                                                                      filename=filename)
