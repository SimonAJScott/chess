from enum import Enum


class PieceType(Enum):
    wPAWN = 1
    wROOK = 2
    wKNIGHT = 3
    wBISHOP = 4
    wQUEEN = 5
    wKING = 6
    bPAWN = -1
    bROOK = -2
    bKNIGHT = -3
    bBISHOP = -4
    bQUEEN = -5
    bKING = -6


class Piece:
    location = 0, 0
    pieceType = -1
    color = ''

    def __init__(self, pieceType: PieceType, location, color):
        self.location = location
        self.pieceType = pieceType
        self.color = color

    def possibleMoveLocations(self):
        possibleLocations = ()
        if self.pieceType != 2:
            match self.pieceType:
                case 0:
                    print("its a pawn")
                case 1:
                    print("its a rook")

                case 3:
                    print("its a bishop")
                case 4:
                    print("its a queen")
                case 5:
                    print("its a king")
        else:
            pass
        return possibleLocations

    # def findPawnLocations(self, possibleLocations):
    #     locations = possibleLocations
    #     for i in range(self.location,)
