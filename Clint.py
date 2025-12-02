import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = input("Enter server IP address: ")  # e.g., 192.168.1.5
client.connect((server_ip, 12345))

while True:
    message = input("You: ")
    client.send(message.encode())
    
    if message.lower() == 'bye':
        break

    reply = client.recv(1024).decode()
    print("Server:", reply)

client.close()
