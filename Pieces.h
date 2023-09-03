#pragma once
using namespace std;
#include "Board.h"
#include <iostream>

bool isSpaceFilled(char name, Board tempBoard);
class Piece{
    public:
    int id;
    pair<int, int> location;
    char name;
    bool color;
    bool alive;
    Piece(Board theBoard);
    void initializePieces();
};
class Pawn{
    public:
    pair <int, int> move(char alphabet, int number);
};