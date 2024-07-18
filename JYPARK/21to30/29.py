def solution(enroll, referral, seller, amount):
    answer = []
    tree_table = { }
    seller_table = { }
    money_talbe = { }
    #tree_table 작성 (key : 추천 받은 자, value : 추천 해준 자)
    for i in range(len(enroll)):
        money_talbe[enroll[i]] = 0
        if referral[i] != '-':
            tree_table[enroll[i]] = referral[i]
        else:
            tree_table[enroll[i]] = '-'

    for j in range(len(seller)):
        money = int(amount[j] * 100)
        while True:
            #추천자가 없는 경우
            if tree_table[seller[j]] == '-':
                money_talbe[seller[j]] += money - int(money * 0.1)
                break
            #추천자가 있는 경우
            else:
                money_talbe[seller[j]] += int(money - money * 0.1)
                seller[j] = tree_table[seller[j]]
                money = money * 0.1
    for k in money_talbe:
        answer.append(int(money_talbe[k]))   
    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["sam", "emily", "jaimie", "edward"]
amount = [2, 3, 5, 4]
print(solution(enroll, referral, seller, amount))