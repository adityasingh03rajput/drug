import socket

def connect_to_server(host, port, game_id):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))  # Connect to localtunnel URL
    client.send(game_id.encode('utf-8'))
    return client

def main():
    host = input("https://cold-cases-hang.loca.lt")
    port = 5555  # Default port for the game server
    game_id = input("Enter the game ID provided by the host: ")
    
    client_socket = connect_to_server(host, port, game_id)
    if client_socket:
        # Game logic here (same as before)
        pass

if __name__ == "__main__":
    main()
