import paramiko
import threading
import subprocess




def ssh_command(ip,user,passwd,command):
    client = paramiko.SSHClient()
    client.connet(ip,username=user,password=passwd)
    ssh_session =   client.get_transport().open_session()
    if(ssh_session.active):
        ssh_session.exec_command(command)
        print(ssh_session.recv(1024))
    

