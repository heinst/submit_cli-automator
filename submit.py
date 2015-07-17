#! /usr/bin/env python

import paramiko
import getpass
import sys
import os
from scp import SCPClient

try:
    pathToUpload = sys.argv[1]
except:
    print 'No path to file to upload provided as first argument'
    sys.exit(1)

try:
    tuxPathForFile = sys.argv[2]
except:
    print 'No tux path provided as second argument'
    sys.exit(1)

username = raw_input('Enter username: ')

p = getpass.getpass()

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('tux.cs.drexel.edu', username=username, password=p)

if(os.path.isdir(pathToUpload)):

    scp = SCPClient(ssh.get_transport())
    scp.put(pathToUpload, remote_path=tuxPathForFile, recursive=True)

else:
    scp = SCPClient(ssh.get_transport())
    scp.put(pathToUpload, remote_path=tuxPathForFile, recursive=False)

classAbbreviation= raw_input('Enter the class abbreviation: ')
assignment = raw_input('Enter the assignment name: ')

stdin, stdout, stderr = ssh.exec_command('cd {0}/{1}'.format(tuxPathForFile, tuxPathForFile.split('/')[-1]))
print stdout.read()
stdin, stdout, stderr = ssh.exec_command('submit_cli -c {0} -a {1} *'.format(classAbbreviation, assignment))
print stdout.readlines()
stdin, stdout, stderr = ssh.exec_command('submit_cli -c {0} --verify'.format(classAbbreviation, assignment))
print stdout.readlines()
ssh.close()
