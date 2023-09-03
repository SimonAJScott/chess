#include <iostream>
#include "Board.h"
using namespace std;

bool isSpaceFilled(char name, Board tempBoard){
    if(name == 'P'){

    }
    if(name == 'R'){

    }
    if(name == 'k'){

    }
    if(name == 'B'){

    }
    if(name == 'Q'){

    }
    if(name == 'K'){

    }
    return true;
}

class Piece{
    public:
    int id;
    pair<int, int> location;
    char name;
    bool color;
    //true = white, false = black
    bool alive;
    public:
    Piece(Board theBoard){
        initializePieces();
    }
    void initializePieces(){

    }
};

class Pawn : public Piece{
    public:
    pair<int, int> move(char alphabet, int number){
        pair<int, int> newLocation;
        //logic needed
        return newLocation;
    }
};

/*
a2 white pawn id = 0
b2 id = 1
c2 id = 2
d2 id = 3
e2 id = 4
f2 id = 5
g2 id = 6
h2 id = 7

a1 white rook id = 8
b1 
*/