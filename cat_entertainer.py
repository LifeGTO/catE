import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Cat Entertainer')

# Load the mouse image
# Ensure there's a mouse.png in the same directory as this script.
mouse_image = pygame.image.load('mouse.png')
mouse_rect = mouse_image.get_rect()

# Set up the colors
WHITE = (255, 255, 255)

# Function to move the mouse to a new random position
def move_mouse():
    mouse_rect.x = random.randint(0, width - mouse_rect.width)
    mouse_rect.y = random.randint(0, height - mouse_rect.height)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(WHITE)
    
    # Move the mouse to a new position every 50 frames
    if pygame.time.get_ticks() % 50 == 0:
        move_mouse()
    
    # Draw the mouse image to the screen
    screen.blit(mouse_image, mouse_rect)
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
