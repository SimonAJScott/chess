class Board:
    board = [[0 for _ in range(8)] for _ in range(8)]

    def printBoard(self):
        for i in range(0, 8):
            print(self.board[i])

    def pixelToArray(self, mouse_pos):
        # row = (mouse_pos[0]-30)//78.75
        # col = (mouse_pos[1]-30)//78.75
        row = (mouse_pos[0]-150)//62.5
        col = (mouse_pos[1]-150)//62.5
        return (row, col)

    def arrayToPixel(self, row, col, offset):
        # row + size of each square + margin + in the center of square + in center of the image (20*20)
        # height = (row)*78.75+30+78.75/2
        height = (row)*62.5+150+62.5/2
        width = (col)*62.5+150+62.5/2
        return (height-offset, width-offset)

    def setup(self):
        # white pieces
        self.board[2][7] = 4
        self.board[5][7] = 4
        self.board[0][7] = 2
        self.board[7][7] = 2
        self.board[3][7] = 6
        self.board[6][7] = 3
        self.board[1][7] = 3
        self.board[4][7] = 5
        for i in range(0, 8):
            self.board[i][6] = 1

        # black pieces
        self.board[2][0] = -4
        self.board[5][0] = -4
        self.board[0][0] = -2
        self.board[7][0] = -2
        self.board[3][0] = -6
        self.board[6][0] = -3
        self.board[1][0] = -3
        self.board[4][0] = -5

        for i in range(0, 8):
            self.board[i][1] = -1

    def getBoard(self):
        return self.board
