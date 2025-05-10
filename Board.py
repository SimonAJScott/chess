class Board:
    board = [[0]*8]*8

    def printBoard(self):
        print(self.board)

    def pixelToArray(self, mouse_pos):
        row = (mouse_pos[0]-30)//78.75
        col = (mouse_pos[1]-30)//78.75
        return row, col

    def arrayToPixel(self, row, col):
        return 0
