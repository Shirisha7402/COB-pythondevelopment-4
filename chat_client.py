import socket
import threading

# Server configuration
server_address = ('192.168.43.5', 12345)  # Replace with the server's IP and port

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

# Function to send messages
def send_message():
    while True:
        message = input()
        client_socket.send(message.encode())

# Function to receive messages
def receive_messages():
    while True:
        message = client_socket.recv(1024).decode()
        print(message)

# Create separate threads for sending and receiving messages
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_messages)

send_thread.start()
receive_thread.start()
