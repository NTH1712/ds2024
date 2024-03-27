import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = socket.gethostname()
port = 12345  # Reserve a port for your service.

# Bind to the port
server_socket.bind((host, port))

# Now wait for client connection.
server_socket.listen(5)  # Allow 5 connections to queue up

print("Server listening on {}:{}".format(host, port))

while True:
    # Establish connection with client.
    client_socket, addr = server_socket.accept()
    print('Got connection from', addr)

    # Send a thank you message to the client.
    client_socket.send(b'Thank you for connecting')

    # Close the connection
    client_socket.close()
