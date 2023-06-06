# def solution(scoville, K):
#     answer = 0
#     return answer
import heapq
def solution(scoville, K):
    answer = 0
    q = []
    for i in scoville:
        heapq.heappush(q,i)
    while q[0]<K:
        first = heapq.heappop(q)
        if not q:
            return -1
        second = heapq.heappop(q)
        heapq.heappush(q,first+second*2)
        answer+=1
    return answer