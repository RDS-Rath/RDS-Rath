import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
PACMAN_SIZE = 20
FPS = 15

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Directions
DIRECTIONS = [(0, -PACMAN_SIZE), (0, PACMAN_SIZE), (-PACMAN_SIZE, 0), (PACMAN_SIZE, 0)]

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Self-playing Random Pacman")

# Pacman class
class Pacman:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.direction = random.choice(DIRECTIONS)

    def move(self):
        dx, dy = self.direction
        self.x = (self.x + dx) % SCREEN_WIDTH
        self.y = (self.y + dy) % SCREEN_HEIGHT

    def draw(self):
        pygame.draw.rect(screen, YELLOW, (self.x, self.y, PACMAN_SIZE, PACMAN_SIZE))

# Game loop
def game_loop():
    pacman = Pacman()
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pacman.move()
        pacman.direction = random.choice(DIRECTIONS)

        screen.fill(BLACK)
        pacman.draw()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Run the game
if __name__ == "__main__":
    game_loop()
