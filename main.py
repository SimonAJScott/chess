import pygame
import sys
from Board import Board

pygame.init()

board = pygame.image.load("assets/board.jpg")
icon = pygame.image.load("assets/icon.png")

board_width, board_height = board.get_size()
screen = pygame.display.set_mode((board_width, board_height))
pygame.display.set_icon(icon)
pygame.display.set_caption("simon's chess game!")
greycircle = pygame.image.load("assets/greycircle.png")
resized_image = pygame.transform.scale(greycircle, (20, 20))
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # This gives the (x, y) position of the click
            mouse_pos = event.pos
            if (mouse_pos[0] <= 30 or mouse_pos[0] >= 660 or mouse_pos[1] <= 30 or mouse_pos[1] >= 660):
                print("out of bounds")
            else:
                print(f"Mouse clicked at: {mouse_pos}")
                locationInArray = Board.pixelToArray(Board, mouse_pos)
                print(f"in the array at: {locationInArray}")
                print(
                    f"calculated pixel location: {Board.arrayToPixel(Board, locationInArray[0], locationInArray[1])}")
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw the image at (0, 0)
    screen.blit(board, (0, 0))

    for i in range(0, 8):
        for j in range(0, 8):
            screen.blit(resized_image, tuple(
                # subtract 10 from each (icon is 20x20)
                x - 10 for x in Board.arrayToPixel(Board, i, j)))
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
