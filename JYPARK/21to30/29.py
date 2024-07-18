def solution(enroll, referral, seller, amount):
    answer = []
    tree_table = { }
    money_talbe = {name : 0 for name in enroll}

    #tree_table 작성 (key : 추천 받은 자, value : 추천 해준 자)
    for i in range(len(enroll)):
        tree_table[enroll[i]] = referral[i]

    #돈 계산 함수 (While True 대체)
    def culculate_profit(person, money):
        if person == '-' or money < 1:
            return 0
        else:
            money_talbe[person] += money - money//10
            money = money//10
            culculate_profit(tree_table[person], money) 

    for j in range(len(seller)):
        money = amount[j] * 100
        culculate_profit(seller[j], money)
       
    answer = [money_talbe[person] for person in money_talbe]
    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))