import socket


# 1.To create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET: Refers to the address family for IPv4.
# SOCK_STREAM: Refers to TCP connection.

# 2.To create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# AF_INET: Refers to the address family for IPv4.
# SOCK_DGRAM: Referes to UDP .


# --> SERVER SIDE <--

# 3.bind()

# Example:
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to localhost on port 8080
server_socket.bind(('localhost', 8080))

# 4.listen()

# Example:

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(5)  # The server can queue up to 5 connection requests
print("Server is now listening for connections...")

# 5.accept()

# Example: 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(5)

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# --> CLIENT SIDE <-- 

# 6.connect()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server on localhost at port 8080
client_socket.connect(('localhost', 8080))
print("Connected to server")

# 7.send()

message = "Hello, Server!"
client_socket.send(message.encode('utf-8'))
print("Message sent to the server")

# 8.recv()

# Receive up to 1024 bytes of data from the client
data = client_socket.recv(1024)
print(f"Received from client: {data.decode('utf-8')}")

# 9.close()

client_socket.close()
print("Connection closed")

# --> OTHERS <--

# 10. a = setdefaultimeout()
# 11. b = connect_ex()




