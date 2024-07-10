def solution(enroll, refreal, seller, amount):
    money_dict = {} # 사람들의 총 수익을 나타내는 dict
    referral_dict = {} # 사람들의 추천인을 나타내는 dict

    for a, b in zip(enroll, refreal):
        money_dict[a] = 0
        referral_dict[a] = b

    # referral_dict을 활용하여 tree처럼 활용   
    for person, money in zip(seller, amount):
        money *= 100
        # 추천인이 존재하거나 수익이 존재하면 수익의 90%를 본인이, 10%를 추천인이 가져감 
        while money > 0 and person != '-':
            money_dict[person] += money - money // 10
            money = money // 10            
            person = referral_dict[person] # 추천인으로 이동
    
    answer = list(money_dict.values()) # money_dict의 value를 list로 변경
    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))        


       
