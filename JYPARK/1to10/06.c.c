//문제06
#include <stdio.h>
#include <stdlib.h>

int solution(int N, int stages[]){
    int userNum = sizeof(stages);
    int temp;
    int *result = malloc(sizeof(int) * N);
    double *fail_rate = malloc(sizeof(int) * N);

    // stages배열 오름차순 정렬
    for(int  i = 0; i<userNum; i++){
        if(stages[i] > stages[i+1]){
            temp = stages[i];
            stages[i] = stages[i+1];
            stages[i+1] = temp;
        }
    }

    int stageUser = userNum;
    for(int i = 0; i<N; i++){
        int num_count = 0;
        for(int j = 0; j<userNum; j++){
            if(stages[j] == i+1){
                num_count++;
                stageUser--;
            }
            else{
                break;
            }
        }
        fail_rate[i] = (double)(num_count/stageUser);
    }

    //sorted_result에 result배열 복사하기
    double *sorted_result = malloc(sizeof(int) * N);
    for(int i = 0; i<N; i++){
        sorted_result[i] = fail_rate[i];
    }

    //실패율 오름차순 정렬하기
    double temp;
    for(int i = 0; i<N; i++){
        if(sorted_result[i] > sorted_result[i+1]){
            temp = sorted_result[i];
            sorted_result[i] = sorted_result[i+1];
            sorted_result[i+1] = temp;
        }
    }

    //가장 큰 실패율을 갖는 stage번호 알아내기
    for(int i = 0; i<N; i++){
        for(int j = 0; j<N; j++){
            if(sorted_result[i] == fail_rate[j]){
                result[i] = j+1;
                break;
            }
        }
    }

    return result;
}

//각 스테이지의 실패율을 구하고 실패율을 기준으로 내림차순으로 사용자 번호를 정렬해서 반환하면됨.