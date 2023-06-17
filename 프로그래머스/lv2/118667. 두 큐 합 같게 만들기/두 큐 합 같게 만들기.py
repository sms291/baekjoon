from collections import deque
def solution(queue1, queue2):
    answer = -2
    queue1=deque(queue1)
    queue2=deque(queue2)
    total1=sum(queue1)
    total2=sum(queue2)
    total_len=len(queue1)*4
    if (total1+total2)%2!=0:
        answer=-1
    else:
        answer=0
        while(1):
            if total1<total2:
                su=queue2.popleft()
                queue1.append(su)
                total1+=su
                total2-=su
                answer+=1
            elif total1>total2:
                su=queue1.popleft()
                queue2.append(su)
                total1-=su
                total2+=su     
                answer+=1
            else:
                break
            if answer==total_len:
                answer=-1
                break
            
    return answer