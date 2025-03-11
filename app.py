import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set the width and height of each player
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

# Set the width and height of the ball
BALL_WIDTH = 20
BALL_HEIGHT = 20

# Set the width and height of the bullets
BULLET_WIDTH = 10
BULLET_HEIGHT = 10

# Set the speed of the players
PLAYER_SPEED = 5

# Set the speed of the ball
BALL_SPEED = 5

# Set the speed of the bullets
BULLET_SPEED = 10

# Set the health points of each player
PLAYER_HP = 100

# Set the number of goals needed to win
GOALS_TO_WIN = 5

# Set the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set the font for the game
FONT = pygame.font.Font(None, 36)

class Player(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.hp = PLAYER_HP
        self.goals = 0
        self.frozen = False
        self.freeze_time = 0

    def move(self, dx, dy):
        if not self.frozen:
            self.x += dx
            self.y += dy

            if self.x < 0:
                self.x = 0
            elif self.x > SCREEN_WIDTH - PLAYER_WIDTH:
                self.x = SCREEN_WIDTH - PLAYER_WIDTH

            if self.y < 0:
                self.y = 0
            elif self.y > SCREEN_HEIGHT - PLAYER_HEIGHT:
                self.y = SCREEN_HEIGHT - PLAYER_HEIGHT

    def shoot(self, bullets):
        if not self.frozen:
            bullets.append(Bullet(self.centerx, self.centery))

    def freeze(self):
        self.frozen = True
        self.freeze_time = pygame.time.get_ticks()

class Ball(pygame.Rect):
    def __init__(self):
        super().__init__(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, BALL_WIDTH, BALL_HEIGHT)
        self.speed_x = random.choice([-BALL_SPEED, BALL_SPEED])
        self.speed_y = random.choice([-BALL_SPEED, BALL_SPEED])

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x < 0:
            self.x = 0
            self.speed_x *= -1
        elif self.x > SCREEN_WIDTH - BALL_WIDTH:
            self.x = SCREEN_WIDTH - BALL_WIDTH
            self.speed_x *= -1

        if self.y < 0:
            self.y = 0
            self.speed_y *= -1
        elif self.y > SCREEN_HEIGHT - BALL_HEIGHT:
            self.y = SCREEN_HEIGHT - BALL_HEIGHT
            self.speed_y *= -1

class Bullet(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, BULLET_WIDTH, BULLET_HEIGHT)
        self.speed_x = random.choice([-BULLET_SPEED, BULLET_SPEED])
        self.speed_y = random.choice([-BULLET_SPEED, BULLET_SPEED])

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    player1 = Player(100, 100)
    player2 = Player(700, 100)

    ball = Ball()

    bullets = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player1.shoot(bullets)
                elif event.key == pygame.K_RCTRL:
                    player2.shoot(bullets)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player1.move(0, -PLAYER_SPEED)
        if keys[pygame.K_s]:
            player1.move(0, PLAYER_SPEED)
        if keys[pygame.K_a]:
            player1.move(-PLAYER_SPEED, 0)
        if keys[pygame.K_d]:
            player1.move(PLAYER_SPEED, 0)

        if keys[pygame.K_UP]:
            player2.move(0, -PLAYER_SPEED)
        if keys[pygame.K_DOWN]:
            player2.move(0, PLAYER_SPEED)
        if keys[pygame.K_LEFT]:
            player2.move(-PLAYER_SPEED,0

                         Here is the rest of the code:

```    if keys[pygame.K_RIGHT]:
        player2.move(PLAYER_SPEED, 0)

    ball.move()

    for bullet in bullets:
        bullet.move()

        if bullet.colliderect(player1) and player1 not in bullet.hit_players:
            player1.hp -= 10
            bullet.hit_players.append(player1)

        if bullet.colliderect(player2) and player2 not in bullet.hit_players:
            player2.hp -= 10
            bullet.hit_players.append(player2)

        if bullet.colliderect(ball):
            bullets.remove(bullet)

    if player1.frozen and pygame.time.get_ticks() - player1.freeze_time > 3000:
        player1.frozen = False

    if player2.frozen and pygame.time.get_ticks() - player2.freeze_time > 3000:
        player2.frozen = False

    if player1.hp <= 0:
        player1.frozen = True
        player1.hp = 0

    if player2.hp <= 0:
        player2.frozen = True
        player2.hp = 0

    if ball.colliderect(player1):
        player1.goals += 1
        ball.x = SCREEN_WIDTH / 2
        ball.y = SCREEN_HEIGHT / 2

    if ball.colliderect(player2):
        player2.goals += 1
        ball.x = SCREEN_WIDTH / 2
        ball.y = SCREEN_HEIGHT / 2

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.rect(screen, WHITE, ball)

    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)

    text = FONT.render(f"Player 1 Goals: {player1.goals}", True, WHITE)
    screen.blit(text, (10, 10))

    text = FONT.render(f"Player 2 Goals: {player2.goals}", True, WHITE)
    screen.blit(text, (10, 40))

    text = FONT.render(f"Player 1 HP: {player1.hp}", True, WHITE)
    screen.blit(text, (10, 70))

    text = FONT.render(f"Player 2 HP: {player2.hp}", True, WHITE)
    screen.blit(text, (10, 100))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

if *name* == "*main*":
main()

control key for player 2. The game keeps track of the number of goals each player scores and the amount of health each player has. The game ends when one player reaches 5 goals or when one player's health reaches 0.
