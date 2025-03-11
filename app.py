import socket
import pygame
import math
import random

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
FRICTION = 0.90
BALL_FRICTION = 0.97
BULLET_SPEED = 8
PLAYER_SPEED = 3
BULLET_DAMAGE = 20
FREEZE_TIME = 180
GOAL_SCORE = 5
BALL_IMPACT_MULTIPLIER = 1.2
BALL_BOUNCE = 0.8
DAMAGE_DECAY = 0.01
AUTO_AIM_PLAYER = 1
AUTO_AIM_BALL = 2
NO_AUTO_AIM = 0

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Soccer Shooter Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)

def connect_to_server(host, port, game_id):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))  # Connect to the server
    client.send(game_id.encode('utf-8'))  # Send the game ID to the server
    return client

def main():
    # Get the localtunnel URL and game ID from the user
    localtunnel_url = input("Enter the localtunnel URL (e.g., https://your-subdomain.loca.lt): ")
    game_id = input("Enter the game ID provided by the host: ")
    
    # Extract host and port from the localtunnel URL
    host = localtunnel_url.split("//")[1].split(":")[0]  # Extract host
    port = 5555  # Default port for the game server
    
    # Connect to the server
    client_socket = connect_to_server(host, port, game_id)
    if client_socket:
        print("Connected to the server!")
        # Game logic here (same as before)
    else:
        print("Failed to connect to the server.")

if __name__ == "__main__":
    main()
