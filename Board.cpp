#include <iostream>
#include <cstring>
#include "Board.h"
using namespace std;

class Board{
    public:
    string wholeBoard[8][8];
    Board(){
        initializeBoard();
    }
    void initializeBoard(){
        for(int i = 0; i<8; i++){
            cout << " "<< abs(i-8);
            for(int j = 0; j<8; j++){
                wholeBoard[i][j]="∎";
                //cout << " " << i << "," << j;
                cout << " ";
                cout << wholeBoard[i][j];
            }
            
            cout << endl;
        }
        cout << "   a b c d e f g h" << endl;
    }
    

    void printBoard(){
        for(int i = 0; i<8; i++){
            cout << " "<< abs(i-8);
            for(int j = 0; j<8; j++){
                cout << " ";
                cout << wholeBoard[i][j];
            }
            
            cout << endl;
        }
        cout << "   a b c d e f g h" << endl;
    }
    
};

public: pair<int, int> getLocation(char alphabet, int number){
    pair<int, int> temp = make_pair(abs(number-8), int(alphabet)-97);
    cout << temp.first << " " << temp.second << endl;
    return temp;
}
//❏
//∎
//♙
//♖
//♗

