import pygame as pg
import random
# Initialize Pygame
pg.init()

# Game Constants
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Dodge the Falling Blocks")

# Player Settings
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 60
player_speed = 5

# Obstacle settings
obstacle_width = 50
obstacle_height = 50
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 4

# Game Loop
running = True
while running:
    pg.time.Clock().tick(60) # Control game fps

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pg.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

        # Move Obstacle
    obstacle_y += obstacle_speed

        # Reset Obstacle if it fall of the screen
    if obstacle_y > HEIGHT:
        obstacle_y = -obstacle_height
        obstacle_x = random.randint(0, WIDTH - obstacle_width)

            # Collision Detection
    if (player_x < obstacle_x + obstacle_width and
        player_x + player_size > obstacle_x and
        player_y < obstacle_y + obstacle_x and
        player_y + player_size > obstacle_y):
        print("Game Over!")
        running = False

    # Draw Everything
    screen.fill(WHITE)
    pg.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    pg.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
    pg.display.update()

# Quit Game
pg.quit()