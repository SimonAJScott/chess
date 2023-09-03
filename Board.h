#pragma once
using namespace std;
class Board{
    public:
    string wholeBoard[8][8];
    void initializeBoard();
    void printBoard();
};
pair<int, int> getLocation(char alphabet, int number);