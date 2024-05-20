def solution(num) :
    digit = []
    while num > 0:
        id = num % 2
        digit.append(str(id))
        num //= 2
    digit.reverse()
    return ''.join(digit)  #여기에서 좀 걸림

print(solution(10)) #반환값 :  1010
print(solution(27)) #반환값 :  11011
print(solution(12345)) #반환값 : 11000000111001