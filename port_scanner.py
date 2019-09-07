import socket
import sys
import subprocess
from datetime import datetime
subprocess.call("exit 1", shell=True)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = input('Target host name:')
port_range_min = int(input('Enter port range inital:'))
port_range_max = int(input('Enter port range end:'))
print(70*"-")
print("Please wait scanning the port of",host_name)
t1 = datetime.now()
host_ip = socket.gethostbyname(host_name)
print(host_name,'host ip:', host_ip)
print(70*"-")
i = 0


def scanner(port):
    try:
        sock.connect((host_ip, port))
        return True

    except:
        return False


try:
    for port_number in range(port_range_min, port_range_max):
        print("Scanning port", port_number)
        if scanner(port_number):
            print('Port', port_number, 'is open')
            i = +1
    t2 = datetime.now()
    total_time = t2 - t1
    print('Number of open port found:', i)
    print("Results found in:", total_time)
    sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()