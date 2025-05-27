from itertools import permutations

# need to give pieces classes with if moved yet


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
        return (int(row), int(col))

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

    def getPossibleLocations(self, location):
        possibleLocations = set()
        row = location[0]
        col = location[1]
        match self.board[row][col]:
            # white pawn
            case 1:
                if col > 0 and self.board[row][col-1] == 0:
                    possibleLocations.add((row, col-1))
                    if 0 < row < 7:
                        if self.board[row+1][col-1] < 0:
                            possibleLocations.add((row+1, col-1))
                        if self.board[row-1][col-1] < 0:
                            possibleLocations.add((row-1, col-1))
            # black pawn
            case -1:
                if col < 7 and self.board[row][col+1] == 0:
                    possibleLocations.add((row, col+1))
                    if 0 < row < 7:
                        if self.board[row+1][col+1] > 0:
                            possibleLocations.add((row+1, col+1))
                        if self.board[row-1][col+1] > 0:
                            possibleLocations.add((row-1, col+1))
            # white rook
            case 2:
                possibleLocations |= self.checkUntilPieceOrEdge(
                    self, ['up', 'down', 'left', 'right'], 'white', location)
            # black rook
            case -2:
                possibleLocations |= self.checkUntilPieceOrEdge(
                    self, ['up', 'down', 'left', 'right'], 'black', location)
            # # white knight
            case 3:
                tempLocations = set()
                for perm in permutations([2, 1, -1, -2], 2):
                    if not ((perm[0] == 2 and perm[1] == -2) or
                            (perm[0] == -2 and perm[1] == 2) or
                            (perm[0] == 1 and perm[1] == -1) or
                            (perm[0] == -1 and perm[1] == 1)):
                        tempLocations.add((row+perm[0], col+perm[1]))
                for tempLocation in tempLocations:
                    if -1 < tempLocation[0] < 8 and -1 < tempLocation[1] < 8 and self.board[tempLocation[0]][tempLocation[1]] <= 0:
                        possibleLocations.add((tempLocation))
            # black knight
            case -3:
                tempLocations = set()
                for perm in permutations([2, 1, -1, -2], 2):
                    if not ((perm[0] == 2 and perm[1] == -2) or
                            (perm[0] == -2 and perm[1] == 2) or
                            (perm[0] == 1 and perm[1] == -1) or
                            (perm[0] == -1 and perm[1] == 1)):
                        tempLocations.add((row+perm[0], col+perm[1]))
                for tempLocation in tempLocations:
                    if -1 < tempLocation[0] < 8 and -1 < tempLocation[1] < 8 and self.board[tempLocation[0]][tempLocation[1]] >= 0:
                        possibleLocations.add((tempLocation))

        return possibleLocations

    def movePiece(self, location, newLocation):
        pieceNum = self.board[location[0]][location[1]]
        self.board[location[0]][location[1]] = 0
        self.board[newLocation[0]][newLocation[1]] = pieceNum

    def checkUntilPieceOrEdge(self, directions, color: str, startLocation: tuple):
        possibleLocations = set()
        for direction in directions:
            match direction:
                case 'up':
                    for i in range(startLocation[1]-1, -1, -1):
                        if (self.board[startLocation[0]][i] != 0):
                            if (color == "black" and self.board[startLocation[0]][i] > 0) or (color == "white" and self.board[startLocation[0]][i] < 0):
                                possibleLocations.add((startLocation[0], i))
                            break
                        possibleLocations.add((startLocation[0], i))
                case 'down':
                    for i in range(startLocation[1]+1, 8):
                        if (self.board[startLocation[0]][i] != 0):
                            if (color == "black" and self.board[startLocation[0]][i] > 0) or (color == "white" and self.board[startLocation[0]][i] < 0):
                                possibleLocations.add((startLocation[0], i))
                            break
                        possibleLocations.add((startLocation[0], i))
                case 'right':
                    for j in range(startLocation[0]+1, 8):
                        if (self.board[j][startLocation[1]] != 0):
                            if (color == "black" and self.board[j][startLocation[1]] > 0) or (color == "white" and self.board[j][startLocation[1]] < 0):
                                possibleLocations.add((j, startLocation[1]))
                            break
                        possibleLocations.add((j, startLocation[1]))
                case 'left':
                    for j in range(startLocation[0]-1, -1, -1):
                        if (self.board[j][startLocation[1]] != 0):
                            if (color == "black" and self.board[j][startLocation[1]] > 0) or (color == "white" and self.board[j][startLocation[1]] < 0):
                                possibleLocations.add((j, startLocation[1]))
                            break
                        possibleLocations.add((j, startLocation[1]))
        return possibleLocations
