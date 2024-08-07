def solution(s):
    answer = ''
    arr = [0 for _ in range(26)]

    for i in s:
        arr[ord(i) - ord('a')] += 1
    
    for i in range(26):
        while arr[i] > 0:
            answer += chr(i + ord('a'))
            arr[i] -= 1
    
    return answer

print(solution("algorithm"))