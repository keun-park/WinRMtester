#!/usr/bin/env python

#Requires pywinrm (pip install pywinrm)
#endpoint is the hostname or ip address of the Windows machine
#transport can be ssl or ntlm
#Runs "ipconfig /all" on the remote host

from winrm.protocol import Protocol
import sys

#====================================================================================================
#You can enter the IP for testing as the first arg eg "./winrmtest.py x.x.x.x" or it will ask you
#If you are going to be using the tester for one IP only you canjust delete this and set the IP variable 

try:
    ip = sys.argv[1]
    
except IndexError:
    ip = raw_input("Enter IP: ")

print(ip)
#====================================================================================================


p = Protocol(
    endpoint='https://' + ip + ':5986/wsman',
    transport='ssl',

#====================================================================================================
#Username and Password on the VM you are testing 
    username='crcadmin',
    password='8dN3n2%bD73Z483!nbSg',
#====================================================================================================

    server_cert_validation='ignore')
shell_id = p.open_shell()
command_id = p.run_command(shell_id, 'ipconfig', ['/all'])
std_out, std_err, status_code = p.get_command_output(shell_id, command_id)
p.cleanup_command(shell_id, command_id)
print(std_out, status_code)
