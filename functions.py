import socket, os
from resources import *

sock = socket.socket()


def get_load_average(client):
    sshclient = client
    stdin, stdout, stderr = sshclient.exec_command("top -b -n 1 | grep 'load average' | awk '{ print $12 $13 $14}'")
    data = stdout.read().decode("utf-8") + stderr.read().decode("utf-8")
    print(f"Load average is: {data}")


def get_memory(client):
    sshclient = client
    stdin, stdout, stderr = sshclient.exec_command("free -m")
    data = str(stdout.read().decode("utf-8") + stderr.read().decode("utf-8")).split(" ")
    total_mem = data[51]
    used_mem = data[60]
    free_mem = data[69]
    buff_mem = data[84]
    swap = data[100]
    print(f"Memory info\nTotal memory: {total_mem}\nCurrently used memory: {used_mem}\n"
          f"Free memory: {free_mem}\nMemory in cache: {buff_mem}\nSwap space: {swap}")


def ping_check(argv):
    host = argv[1]
    hostname = socket.gethostbyaddr(host)[0]
    if os.system("ping -c 1 " + hostname + " > /dev/null") == 0:
        print("Server responds to ping via hostname")
    else:
        print("Server does not respond to ping via hostname")

    if os.system("ping -c 1 " + host + " > /dev/null") == 0:
        print("Server responds to ping via IP")
    else:
        print("Server does not respond to ping via IP")

    try:
        sock.connect((host, http_port))
        print("The connection via HTTP has been successful.")
    except:
        print("The connection to HTTP port has failed")
