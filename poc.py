# 需要自行修改 ip_address
# 代码中的循环是一开始用于测试的，没有实际用途

import socket, time

base_path = ".\\data\\"
ip_address = "192.168.183.101"
port = 1801

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip_address, port))

f = open(base_path + "establish_connection.bin", "rb")
ec = f.read()
f.close()

f = open(base_path + "connection_parameters.bin", "rb")
cp = f.read()
f.close()

f = open(base_path + "user_message.bin", "rb")
um = f.read()
data = bytearray(um)
f.close()

#f = open(base_path + "session_acknowledgment.bin", "rb")
#sa = f.read()
#f.close()

for i in range(0, 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip_address, port))
    
    sock.sendall(ec)
    print("[+] Establish connection.")
    sock.recv(1024)
    print("[+] Receive data done.")

    sock.sendall(cp)
    print("[+] Connection parameters.")
    sock.recv(1024)
    print("[+] Receive data done.")

    #data[0x5e] = i
    #data[0x5f] = 0xff
    sock.sendall(data)
    print("[+] User message.")
    sock.recv(1024)
    print("[+] Receive data done.")

    #sock.sendall(sa)
    #print("[+] Session acknowledgment.")
    #sock.recv(1024)
    #print("[+] Receive data done.\n")

    sock.close()

    time.sleep(0.1)
    
