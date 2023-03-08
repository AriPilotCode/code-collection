import socket
import random
import time

SERVER_IP = "127.0.0.1"
PORT = 8821
MAX_MSG_SIZE = 1024
SERIAL_NUMBER_FIELD_SIZE = 4
MAX_SERIAL_NUM = 10000
TIMEOUT_IN_SECONDS = 5
LIST_OF_SERIAL = []

def special_sendto(socket_object, response, client_address):
    fail = random.randint(1, 3)
    if not (fail == 1):
        socket_object.sendto(response.encode(), client_address)
    else:
        print("Oops")


my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = 'EXIT'
request_serial_number = 0
data = ''
while 'EXIT' not in data:

    serial_number_field = str(request_serial_number).zfill(SERIAL_NUMBER_FIELD_SIZE)
    special_sendto(my_socket,serial_number_field + msg , (SERVER_IP, PORT))
    my_socket.settimeout(TIMEOUT_IN_SECONDS)

    try:
        (response, remote_address) = my_socket.recvfrom(MAX_MSG_SIZE)
        data = response.decode()
        print("The server sent " + data)
        request_serial_number += 1

    except:
        print('this code is reached despite the server is not answering')

    if request_serial_number == MAX_SERIAL_NUM:
        request_serial_number = 0


my_socket.close()
