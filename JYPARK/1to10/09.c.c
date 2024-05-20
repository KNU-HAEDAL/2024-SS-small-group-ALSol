//문제09

#include <stdio.h>
#include <stdlib.h>

int solution(int N){
    int *binary;
    int i = 0;
    int quotient;
    
    while(quotient != 0){
        binary = malloc(sizeof(int));
        binary[i] = N % 2;
        i++;
        quotient = N / 2;
    }

    int result[sizeof(binary)];
    int j = 0;
    for(int i = sizeof(binary)-1 ; i>=0 ; i--){
        result[j] = binary[i];
        j++;
    }
    free(binary);
    return result;
}