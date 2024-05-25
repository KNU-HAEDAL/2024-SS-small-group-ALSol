def solution(n):
    binary_number = ''  
    while n > 0:
        remainder = n % 2  
        binary_number = str(remainder) + binary_number  
        n = n // 2 

    return binary_number if binary_number else '0'
