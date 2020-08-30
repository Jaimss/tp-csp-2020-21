import socket

HEADER = 64
PORT = 5050
SERVER = '192.168.254.12'
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '-disconnect'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(msg)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


disconnected = False
while not disconnected:
    m = input("Message: ")
    if m.lower() is DISCONNECT_MESSAGE:
        send(m)
        break
    send(m)
