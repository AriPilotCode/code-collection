import socket
import random
import time

SERIAL_NUMBER_FIELD_SIZE = 4
MAX_SERIAL_NUM = 10000
SERVER_IP = "0.0.0.0"
PORT = 8821
MAX_MSG_SIZE = 1024
LIST_OF_SERIAL = []

def special_sendto(socket_object, response, client_address):
    fail = random.randint(1, 3)
    if not (fail == 1):
        socket_object.sendto(response.encode(), client_address)
    else:
        print("Oops")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, PORT))
data = ''

while 'EXIT' not in data:

    (client_message, client_address) = server_socket.recvfrom(MAX_MSG_SIZE)
    data = client_message.decode()
    print("Client sent: " + data)
    response = data[3:]
    client_serial = data[:3]
    special_sendto(server_socket, client_serial+response, client_address)

server_socket.settimeout(2)
special_sendto(server_socket, 'EXIT', client_address)
server_socket.settimeout(2)
special_sendto(server_socket, 'EXIT', client_address)


server_socket.close()
