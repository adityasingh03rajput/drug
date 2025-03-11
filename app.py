import socket
import random
import threading

def handle_client(client_socket, addr, player_data, code):
    client_socket.send(code.encode('utf-8'))  # Send the code to the client
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            # Update player data based on received data
            player_data[addr] = data
            # Send updated player data to both clients
            for client in clients:
                client.send(str(player_data).encode('utf-8'))
        except:
            break
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.50.185', 5555))
    server.listen(2)
    print("Server started. Waiting for connections...")
    
    # Generate a random 4-digit code
    code = str(random.randint(1000, 9999))
    print(f"Game Code: {code}")
    
    player_data = {}
    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        print(f"Connection from {addr} established.")
        threading.Thread(target=handle_client, args=(client_socket, addr, player_data, code)).start()

clients = []
start_server()
