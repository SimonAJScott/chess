class Board:
    board = [[0]*8]*8

    def printBoard(self):
        print(self.board)

    def pixelToArray(self, mouse_pos):
        row = (mouse_pos[0]-30)//78.75
        col = (mouse_pos[1]-30)//78.75
        return (row, col)

    def arrayToPixel(self, row, col):
        # row + size of each square + margin + in the center of square + in center of the image (20*20)
        height = (row)*78.75+30+78.75/2
        width = (col)*78.75+30+78.75/2
        return (height, width)

    def getBoard(self):
        return self.board
