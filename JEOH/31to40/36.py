def solution(phone):
    phone.sort()
    for i in range(len(phone)-1):
        if phone[i+1].startswith(phone[i]):
            return False
    return True