import sys, socket, os, paramiko, threading
from functions import *
from resources import *


def checks(argv):
    host = argv[1]
    ping_check(sys.argv)
    sshclient = paramiko.SSHClient()
    sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    if argv[2] == "22":
        sshclient.connect(hostname=host, username='root', password=argv[3], port=argv[2])
        get_load_average(sshclient)
        get_memory(sshclient)
    elif argv[2] == "21098":
        sshclient.connect(hostname=host, username='root', key_filename=key_path, port=21098)
        get_load_average(sshclient)
        get_memory(sshclient)


checks(sys.argv)
