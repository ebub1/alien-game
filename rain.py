import pygame
import random

# Setting window parameters
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rain")

# Setting background color
bg_color = (200, 200, 200)

# Loading the drop image
drop_image = pygame.image.load("drop.png")

# Creating a list of drops
drops = []
for i in range(100):
    x = random.randint(0, width)
    y = random.randint(-height, 0)
    drops.append([x, y])

# Main game loop
while True:
    # Handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Drawing the frame
    screen.fill(bg_color)
    for drop in drops:
        screen.blit(drop_image, drop)
        drop[1] += 1  # Moving the drop down
        if drop[1] > height:  # If the drop reaches the bottom
            drops.remove(drop)  # Removing the drop from the list
            x = random.randint(0, width)
            y = random.randint(-height, 0)
            drops.append([x, y])  # Adding a new drop
    pygame.display.update()
