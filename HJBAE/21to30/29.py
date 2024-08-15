"""
모든 판매원은 칫솔 판매로 생기는 이익에서 10%를 계산해 자신을 조직에 참여시킨 추천인에게 배분 나머지는 자신이 가짐
모든 판매원은 자신이 조직에 추천하여 가입시킨 판매원의 이익금의 10%를 자신이 가짐
10% 계산할 때 원 단위에서 자르고, 10% 계산한 금액이 1원 미만이면 분배 X
"""

# 판매원 얻은 이익 계산하고 10%를 추천인에게 분배
def distribute_profit(name, profit, parent, earnings):
    if name == "-" or profit == 0:    # 추천인 "-"이거나 분배할 이익이 1원 미만이면 종료
        return
    parent_profit = profit // 10
    earnings[name] += profit - parent_profit
    distribute_profit(parent[name], parent_profit, parent, earnings)


def solution(enroll, referral, seller, amount):
    # 일단 돈 줘야 하는 사람을 key로, 받는 사람을 value로 대응시켜서 저장
    parent = {enroll[i] : referral[i] for i in range(len(enroll))}    # 추천인 저장
    earnings = {name : 0 for name in enroll}    # 각 seller 총 수익 저장하는 dictionary

    for i in range(len(seller)):
        profit = amount[i] * 100
        seller_info = seller[i]
        distribute_profit(seller[i], profit, parent, earnings)

    return [earnings[name]for name in enroll]


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]

seller1 = ["young", "john", "tod", "emily", "mary"]
amount1 = [12, 4, 2, 5, 10]

seller2 = ["sam", "emily", "jaimie", "edward"]
amount2 = [2, 3, 5, 4]
# result1 = [360, 958, 108, 0, 450, 18, 180, 1080]

print(solution(enroll, referral, seller1, amount1))
# result2 = [0, 110, 378, 180, 270, 450, 0, 0]

print(solution(enroll, referral, seller2, amount2))