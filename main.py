# Simple pygame program

# Import and initialize the pygame library
import pygame
from data.object import GameObject
from data.collision import check_collision

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
object1 = GameObject(100, 100, "resources/images/Slime.png")
object2 = GameObject(200, 100, "resources/images/Slime.png")
object3 = GameObject(300, 100, "resources/images/Slime.png")

objects = [object1, object2, object3]

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))
    check_collision(objects)
    object1.move(0.1)
    object1.render(screen)
    object2.render(screen)
    object3.render(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
