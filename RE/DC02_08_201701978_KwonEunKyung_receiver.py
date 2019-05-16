import socket
import struct

ip_address = '192.168.0.7'
port_number = 3600

server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server_sock.bind((ip_address, port_number))
data_transferred = 0

check = 0
data_file_size = 0

while True:
    data, address = server_sock.recvfrom(2000)

    if data == b'end sign':
        receive_file.close()
        server_sock.close()
        break

    if check is 0:
        data_file_name = data.decode()
        print("File Name: ",data_file_name)
        receive_file = open (data_file_name,'wb')
        check += 1

    elif check is 1:
        data_file_size = int(data.decode())
        print("File Size: ",data_file_size)
        check += 1

    elif check > 1:
        receive_file.write(data)
        data_transferred += len(data)        


        print("(current Size / total size) = ", data_transferred,"/" , data_file_size , " , ", data_transferred/data_file_size*100, " %")


                
