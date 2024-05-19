#include <stdio.h>

int solution(int answer[]){ 
    int count = 0;
    int index = 0;
     int score[] = {0};
     int result[] = {0};
     int player1[] = {1, 2, 3, 4, 5}; //5
     int player2[] = {2, 1, 2, 3, 2, 4, 2, 5}; //8
     int player3[] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}; //10

//player1의 정답 개수
    for(int i = 0; i < sizeof(answer); i++){
        if(answer[i] == player1[index]){
            count++;
        } 
        index++; 
        if(index == 5){
             index = 0;
         }
        
    }
    score[0] = count;

//player2의 정답 개수
    for(int i = 0; i < sizeof(answer); i++){
        if(answer[i] == player2[index]){
            count++;
        } 
        index++; 
        if(index == 8){
             index = 0;
         }
        
    }
    score[1] = count;

//player3의 정답 개수
    for(int i = 0; i < sizeof(answer); i++){
        if(answer[i] == player3[index]){
            count++;
        } 
        index++; 
        if(index == 10){
             index = 0;
         }
        
    }
    score[2] = count;

    //점수 최댓값 구하기
     int hihest_score = 0;
     for(int i = 1; i<3; i++){
        hihest_score = score[0];
        if(score[i] > hihest_score){
            hihest_score = score[i];
        }
     }

    //점수 최댓값 가지는 player구하기
     index = 0;
     for(int i = 0; i<3;i++){
        if(score[i] == hihest_score){
            result[index] = i+1;
        }
     }
     return result;
}
 

int main(){
    int answers[] = {1, 2, 3, 4, 5};
    int result = solution(answers);
    return 0;
}



/*int solution2(int answer[]){
     int player1[] = {1, 2, 3, 4, 5}; //5
     int player2[] = {2, 1, 2, 3, 2, 4, 2, 5}; //8
     int player3[] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}; //10
     int count = 0;

     for(int i = 0; i< sizeof(answer); i++){
        if(player1[i % sizeof(player1)] == answer[i]){
            count++;
        }
     } 
}*/