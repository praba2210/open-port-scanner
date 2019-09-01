import socket
import sys
from datetime import datetime
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = input('Enter the Target host name:')
port_range = int(input('Enter maximum port range to be scanned:'))
t1 = datetime.now()
host_ip = socket.gethostbyname(host_name)
print('Host ip:', host_ip)

i = 0


def scanner(port):
    try:
        sock.connect((host_ip, port))
        return True

    except:
        return False


try:
    for port_number in range(1, port_range):
        print("Scanning port", port_number)
        if scanner(port_number):
            print('Port', port_number, 'is open')
            i = +1
    t2 = datetime.now()
    total_time = t2 - t1
    print('Number of open port found:', i)
    print("Results found in:", total_time)

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()
