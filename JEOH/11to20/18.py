def fun1(arr,x):
    hashtable=[0]*(x+1)
    for num in arr:
        if num<=x:
            hashtable[num]=1
    return hashtable
def solution(arr,target):
    hashtable=fun1(arr,target)
    for num in arr:
        answer=target-num
        if(answer!=num and answer>=0 and answer<=target and hashtable[answer]==1):
            return True
        return False