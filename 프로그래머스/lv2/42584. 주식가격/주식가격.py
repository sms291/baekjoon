from collections import deque
def solution(prices):
    answer = []
    prices=deque(prices)
    while(len(prices)>0):
        su=prices.popleft()
        cnt=0
        #print(prices)
        for gab in prices:
            if gab>=su:
                cnt+=1
            else:
                cnt+=1
                break
        answer.append(cnt)
    return answer