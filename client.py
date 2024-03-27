import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = socket.gethostname()
port = 12345  # Reserve a port for your service.

# Connect to the server
client_socket.connect((host, port))

# Receive data from the server
data = client_socket.recv(1024)

print("Received message from server:", data.decode())

# Close the connection
client_socket.close()
