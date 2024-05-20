//문제07
#include <stdio.h>
#include <stdlib.h>

int solution(char dirs[]){
    int length = sizeof(dirs);
    int answer = 0;
    int coordinates[100][100]; // (x, y)를 저장할 배열
    int i = 0;
    int x = 5;
    int y = 5;

  

    while(dirs[i] == NULL){
        if(x <= 0 || x > 11 || y <= 0 || y > 11){
            return x, y;
        }
        if(dirs[i] == 'L'){
            x--;
            i++;
        }
        if(dirs[i] == 'R'){
            x++;
            i++;
        }
        if(dirs[i] == 'U'){
            y++;
            i++;
        }
        if(dirs[i] == 'D'){
            y--;
            i++;
        }
    }
    


   


}