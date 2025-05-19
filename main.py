import pygame
import sys
from Board import Board


currentBoard = Board.getBoard(Board)
pygame.init()

# board = pygame.image.load("assets/board.jpg")
board = pygame.image.load("assets/chessboardbig.png")
icon = pygame.image.load("assets/icon.png")
board_width, board_height = board.get_size()
screen = pygame.display.set_mode((board_width, board_height))

# loading assets
wBishop = pygame.image.load("assets/w_bishop_1x.png")
wBishop = pygame.transform.scale(wBishop, (50, 50))
wKing = pygame.image.load("assets/w_king_1x.png")
wKing = pygame.transform.scale(wKing, (50, 50))
wQueen = pygame.image.load("assets/w_queen_1x.png")
wQueen = pygame.transform.scale(wQueen, (50, 50))
wKnight = pygame.image.load("assets/w_knight_1x.png")
wKnight = pygame.transform.scale(wKnight, (50, 50))
wRook = pygame.image.load("assets/w_rook_1x.png")
wRook = pygame.transform.scale(wRook, (50, 50))
wPawn = pygame.image.load("assets/w_pawn_1x.png")
wPawn = pygame.transform.scale(wPawn, (40, 40))

bBishop = pygame.image.load("assets/b_bishop_1x.png")
bBishop = pygame.transform.scale(bBishop, (50, 50))
bKing = pygame.image.load("assets/b_king_1x.png")
bKing = pygame.transform.scale(bKing, (50, 50))
bQueen = pygame.image.load("assets/b_queen_1x.png")
bQueen = pygame.transform.scale(bQueen, (50, 50))
bKnight = pygame.image.load("assets/b_knight_1x.png")
bKnight = pygame.transform.scale(bKnight, (50, 50))
bRook = pygame.image.load("assets/b_rook_1x.png")
bRook = pygame.transform.scale(bRook, (50, 50))
bPawn = pygame.image.load("assets/b_pawn_1x.png")
bPawn = pygame.transform.scale(bPawn, (40, 40))

greycircle = pygame.image.load("assets/greycircle.png")
greycircle = pygame.transform.scale(greycircle, (20, 20))


def printBoard():
    for i in range(0, 8):
        for j in range(0, 8):
            match currentBoard[i][j]:
                case 1:
                    screen.blit(wPawn, Board.arrayToPixel(Board, i, j, 20))
                case 2:
                    screen.blit(wRook, Board.arrayToPixel(Board, i, j, 25))
                case 3:
                    screen.blit(wKnight, Board.arrayToPixel(Board, i, j, 25))
                case 4:
                    screen.blit(wBishop, Board.arrayToPixel(Board, i, j, 25))
                case 5:
                    screen.blit(wQueen, Board.arrayToPixel(Board, i, j, 25))
                case 6:
                    screen.blit(wKing, Board.arrayToPixel(Board, i, j, 25))
                case -1:
                    screen.blit(bPawn, Board.arrayToPixel(Board, i, j, 20))
                case -2:
                    screen.blit(bRook, Board.arrayToPixel(Board, i, j, 25))
                case -3:
                    screen.blit(bKnight, Board.arrayToPixel(Board, i, j, 25))
                case -4:
                    screen.blit(bBishop, Board.arrayToPixel(Board, i, j, 25))
                case -5:
                    screen.blit(bQueen, Board.arrayToPixel(Board, i, j, 25))
                case -6:
                    screen.blit(bKing, Board.arrayToPixel(Board, i, j, 25))


pygame.display.set_icon(icon)
pygame.display.set_caption("simon's chess game!")
# Main loop
running = True
setup = True
while running:
    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw the image at (0, 0)
    screen.blit(board, (0, 0))

    if setup:
        Board.setup(Board)
        Board.printBoard(Board)
        setup = False
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # This gives the (x, y) position of the click
            mouse_pos = event.pos
            # min = 30
            # max = 660
            min = 150
            max = 650
            if (mouse_pos[0] <= min or mouse_pos[0] >= max or mouse_pos[1] <= min or mouse_pos[1] >= max):
                print("out of bounds")
            else:
                print(f"Mouse clicked at: {mouse_pos}")
                locationInArray = Board.pixelToArray(Board, mouse_pos)
                print(f"in the array at: {locationInArray}")
                print(
                    f"calculated pixel location: {Board.arrayToPixel(Board, locationInArray[0], locationInArray[1], 0)}")
        if event.type == pygame.QUIT:
            running = False
    printBoard()
    # # subtract 10 from each (icon is 20x20) parameter in arraytopixel
    # for i in range(0, 8):
    #     for j in range(0, 8):
    #         screen.blit(greycircle, (Board.arrayToPixel(Board, i, j, 10)))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
