N=int(input())
from collections import deque

total=[]
for i in range(1,N+1):
    total.append(int(input()))
que=deque(total)
stack=[]
k=1
answer=[]
while(len(que)>0):    
    cnt=0
    if not stack:
        stack.append(k)
        #print('+')
        answer.append('+')
        k+=1
        cnt=1
    else:
        if stack[-1]==que[0]:
            stack.pop()
            que.popleft()
            #print('-')
            answer.append('-')
            cnt=1
        else:
            stack.append(k)
            #print('+')    
            answer.append('+')
            k+=1
            cnt=1   
    if cnt==0 or len(answer)==len(total)*2:
        break        
if answer.count('+')==answer.count('-'):
    for i in answer:
        print(i)
else:
    print('NO')