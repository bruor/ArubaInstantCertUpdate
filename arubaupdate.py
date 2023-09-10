#!/usr/bin/env python3
import paramiko
import time

#define and start session
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('virtual_controller_hostname', username='admin', password='your_password')

#open interactive channel
channel = ssh.invoke_shell()

#declare an output var and receive to it. If this line isn't here, commands can't be sent. 
out = channel.recv(9999)

# Read and send commands from the local file
with open('commandfile.txt', 'r') as file:
    for line in file:
        command = line.strip() + '\r'
        
        if command:
            print(f"Sending command: {command}")
            channel.send(command)
            while not channel.recv_ready():
	            time.sleep(1)

            out = channel.recv(9999)
            print(out.decode("ascii"))
            
ssh.close
