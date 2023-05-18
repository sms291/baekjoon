import time 

start = time.time()

def solution(k, tangerine):
# 답안 작성 부분 ===============
    dic={}
    for i in tangerine:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    box=[]
    for size,number in dic.items():
        box.append([number,size])
    box.sort(reverse=True)
    answer=0
    total=0
    for i in box:
        total+=i[0]
        if total>=k:
            answer+=1
            break
        else:
            answer+=1
   


# ==============================
    return answer