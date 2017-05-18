#!/usr/bin/python

import paramiko 

host = '194.84.228.42'
user = 'root'
secret = 'Passwd02'
port = 7990

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
stdin, stdout, stderr = client.exec_command('ls -l')
data = stdout.read() + stderr.read()
client.close()
