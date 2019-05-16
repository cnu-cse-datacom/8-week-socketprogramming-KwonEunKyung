import socket
import os

serverIP = '192.168.0.7'
serverPort = 3600

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_sock.connect((serverIP, serverPort))
data_transferred = 0


file_name = input("Input File Name: ")
    
file_name_send = client_sock.sendto(file_name.encode(), (serverIP,serverPort))
    
send_file = open(file_name , 'rb')
file_size = os.path.getsize(file_name)
print("file size : ", file_size)
client_sock.sendto(str(file_size).encode(),(serverIP,serverPort))

while True:

    data =  send_file.read(1024)
#    data_transferred += client_sock.sendto(data, (serverIP, serverPort))


    if data == b'':
        client_sock.sendto("end sign".encode(),(serverIP,serverPort))
        send_file.close()
        client_sock.close()
        print("File send end")
        break
    
    data_transferred += client_sock.sendto(data, (serverIP, serverPort))


    print("( current Size / total Size ) = ",data_transferred , "/" , file_size," , ", (data_transferred / file_size)*100, "%")


