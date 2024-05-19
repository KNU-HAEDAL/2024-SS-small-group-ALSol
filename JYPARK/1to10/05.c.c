//문제05
#include <stdio.h>

int solution(int arr1[][100], int arr2[][100]){
    int sum;
    int result[100][100];
    int row = sizeof(arr1) / sizeof(arr1[0]);
    int col = sizeof(arr2[0]) / sizeof(int);
    int arr2_row = sizeof(arr2)/sizeof(arr2[0]);
    

    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            for(int k = 0; k < arr2_row; k++){
                result[i][j] = arr1[i][k] * arr2[k][j];

            }
        }
    }
    return result;
}

/*int main(){
    int test[3][2]; 
    printf("%d", sizeof(test));
    return 0;
} */