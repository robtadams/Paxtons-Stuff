import random
import pygame

def chaosGame():

    # Initialize Pygame
    pygame.display.init()

    # Initialize the Clock
    clock = pygame.time.Clock()

    # Set the dimensions of the window
    windowWidth = 1925
    windowHeight = 1025
    window = pygame.display.set_mode((windowWidth, windowHeight))

    # Set the window captain and window color
    pygame.display.set_caption("Chaos Game")
    windowColor = [0, 0, 0]
    window.fill(windowColor)

    # Update the window
    pygame.display.update()

    """Generate three random coordinate points p1, p2, and p3"""

class Point():
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    Point1_X = random.randint(0, 1900)
    Point1_Y = random.randint(0, 1000)
    Point1_size = 100 
    

    """Draw the three random points onto the window"""


    """Find the center of the triangle and draw that point onto the window"""


    """Create a loop for several thousand iterations"""


    """Pick a random vertex from the triangle"""


    """Find the median between your current coordinate point and the coordinate of the chosen vertex"""


    """Update your current coordinate point to be the median point you generated"""


if __name__ == "__main__":
    chaosGame()
