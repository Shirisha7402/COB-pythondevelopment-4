import socket
import threading

# Server configuration
host = '0.0.0.0'  # Listen on all available network interfaces
port = 12345

# Create a socket for server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

# List to store connected clients
clients = []

# Function to broadcast messages to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                # Remove the client if unable to send a message
                remove(client)

# Function to remove a client
def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

# Function to handle a client connection
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"Received: {message.decode()}")
                broadcast(message, client_socket)
            else:
                # Remove the client if the connection is closed
                remove(client_socket)
        except:
            continue

# Main server loop
while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    print(f"Client {client_address} connected")
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
