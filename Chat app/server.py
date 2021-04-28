import socket
import threading

HOST = '127.0.0.1'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

# waiting for connection signal from client
server.listen()

clients = []
nicknames = []


def broadcast(message):
    '''broadcasts the message to all clients'''
    for client in clients:
        client.send(message)


def handle(client):
    '''closes the clients if exception occured, else it calls broadcast functions'''
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[clients.index(client)]} says {message}")
            broadcast(message)

        except:
            index = clients.index(client)
            # removes the client and its name from respective lists
            clients.pop(index)
            client.close()
            nicknames.pop(index)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}!!")

        client.send("NICK".encode('utf-8'))
        # recieves the name for client
        nickname = client.recv(1024).decode('utf-8')

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is: {nickname}")
        broadcast(f"{nickname} connected to the server! \n".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server running..")
receive()
