import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 12345))  # Listen on all IPs, port 12345
server.listen(5)

print("Server started. Waiting for client...")
client_socket, addr = server.accept()
print(f"Connected to {addr}")

while True:
    message = client_socket.recv(1024).decode()
    if message.lower() == 'bye':
        print("Client disconnected.")
        break

    print("Client:", message)
    reply = input("You: ")
    client_socket.send(reply.encode())

client_socket.close()
server.close()
