import socket
import threading

# initial msg will be 64 byte
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '-disconnect'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

prefix = '[MESSENGER]'


def handle_client(conn, addr):
    print(f'{prefix} New Connection: {addr} connected.')

    connected = True
    while connected:
        # blocking
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f'{addr}: {msg}')
            # send back
            conn.send('Msg received'.encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f'{prefix} Listening on {SERVER}:{PORT}')
    while True:
        # blocking
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'{prefix} Active Threads: {threading.active_count() - 1}')


print(f'{prefix} Server is starting...')
start()
