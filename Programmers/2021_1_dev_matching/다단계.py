import collections

def solution(enroll, referral, seller, amount):
    answer = []
    enroll_graph = collections.defaultdict(str)
    revenue_graph = collections.defaultdict(int)
    amount = [element * 100 for element in amount]
    def revenue_calculator(seller, amount):
        if (seller == "-"):
            return
        # 종료 조건
        if (amount <= 0):
            return
        # amount // 10은 원단위 절사 계산하는 방법이다!
        revenue_graph[seller] = revenue_graph[seller] + amount - (amount // 10)
        revenue_calculator(enroll_graph[seller], (amount // 10))
    for i in range(len(enroll)):
        enroll_graph[enroll[i]] = referral[i]
    for j in range(len(seller)):
        revenue_calculator(seller[j], amount[j])
    for k in range(len(enroll)):
        answer.append(revenue_graph[enroll[k]])
    return answer
