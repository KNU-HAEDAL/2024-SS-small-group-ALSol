//문제08
#include <stdio.h>
#define MAX_SIZE 100;

char stack[MAX_SIZE];
int top = -1;

int isEmpty(){
    if(top<0){
        return 1;
    }
    else{
        return 0;
    }
}

int isFull(){
    if(top >= MAX_SIZE - 1){
        return 1;
    }
    else{
        return 0;
    }
}

void push(char input){
    if(isFull){
        printf("Stack is Full.\n");
    }
    else{
        top++;
        stack[top] = input;
    }
}

void pop(char input){
    if(isEmpty){
        printf("Stack is Empty.\n");
    }
    else{
        top--;
    }
}

int solution(char s[]){
    for(int i = 0; i<sizeof(s); i++){
        if(s[i] == '('){
            push('(');
        }
        if(s[i] == ')'){
            pop('(');
        }
    }

    if(top == -1){
        return 1;
    }
    else{
        return 0;
    }
}