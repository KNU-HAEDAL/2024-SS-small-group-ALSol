def solution(n, k):
    answer = 0
    num = ""

    # k진수로 변경
    while n > 0:
        s = str(n % k)
        n = n // k
        num = s + num
    
    # 0으로 나누어 숫자 찾기
    prime = num.split('0')
    
    # 소수인지 판별
    for i in prime:
        # 1 이상의 숫자인지 확인
        if i != '1' and i != '':
            i = int(i)
            check = False

            # 2부터 루트 숫자까지 반복해 소수인지 판별
            for j in range(2, int(i**(1/2))+1):
                if i % j == 0:
                    check = True
                    break
            
            if not check:
                answer += 1
                
    return answer

print(solution(121, 10))