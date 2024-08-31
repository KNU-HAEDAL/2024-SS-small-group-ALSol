def solution(arr, target):
    for num1 in arr:
        if num1 > target:
            continue   # break로 했더니 안 됨..

        elif num1 == target:
            if 0 in arr:
                return True
            else:
                continue
            
        else:
            # target - num1이 num1과 같지 않아야 함!! -> 처리 안 하면 2, 3, 5, 9 // 10에서 빠꾸먹음..
            if (target - num1) in arr and (target - num1) != num1:
                return True
            else:
                continue

    return False

arr = [1, 2, 3, 4, 8]
target = 6
print(solution(arr, target))