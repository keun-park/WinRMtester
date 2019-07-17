#!/usr/bin/env python

#Requires pywinrm (pip install pywinrm)
#endpoint is the hostname ore ip address of the Windows machine
#transport can be ssl or ntlm
#Runs "ipconfig /all" on the remote host

from winrm.protocol import Protocol

p = Protocol(
    endpoint='https://wincl:5986/wsman',
    transport='ssl',
    username='crc',
    password='crc',
    server_cert_validation='ignore')
shell_id = p.open_shell()
command_id = p.run_command(shell_id, 'ipconfig', ['/all'])
std_out, std_err, status_code = p.get_command_output(shell_id, command_id)
p.cleanup_command(shell_id, command_id)
print(std_out, status_code)
