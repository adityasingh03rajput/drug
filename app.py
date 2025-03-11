import socket
import pickle

SERVER_IP = "https://olive-parts-hug.loca.lt"  # Replace with your localtunnel address
SERVER_PORT = 443  # LocalTunnel uses port 443

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, SERVER_PORT))

while True:
    msg = input("Enter message: ")
    client.send(pickle.dumps(msg))
    print("Message sent!")
