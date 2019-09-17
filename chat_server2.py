import socket, traceback

host = str(socket.gethostbyname(socket.gethostname()))
port = 5005
print(host)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('', port))
file=open("C:/Users/Erkan/Desktop/server_name.txt") #Your txt file
data=file.read()
file.close()
while True:
    try:
        message, address = s.recvfrom(8192)
        print ("Got data from",address)
        print(message)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((address[0], 5006))
        sock.send("Server ip: {} // {} ".format(host,data).encode())

    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()