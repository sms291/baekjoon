def solution(people, limit):
    people=sorted(people)
    answer=0
    from collections import deque
    de=deque(people)
    while (len(de)>0):
        if len(de)==1:
            de.pop()
            answer+=1
            break
        if de[0]+de[-1]<=limit:
            de.popleft()
            de.pop()
            answer+=1
        else:
            de.pop()
            answer+=1

    return answer