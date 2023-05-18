from collections import deque
def solution(people, limit):
# 답안 작성 부분 ===============
    answer=0
    people=sorted(people)
    de=deque(people)
    while(len(de)>0):
        if len(de)==1:
            answer+=1
            break
        if de[0]+de[-1]<=limit:
            de.popleft()
            de.pop()
            answer+=1
        else:
            de.pop()
            answer+=1
# ==============================
    return answer