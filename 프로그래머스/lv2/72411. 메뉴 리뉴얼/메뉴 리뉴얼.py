import time
import math
from itertools import combinations
start = time.time()

def solution(orders, course):
# 답안 작성 부분 ===============
    mydict={}
    for numbers in course:
        for k in orders:
            for i in list(combinations(k,numbers)):
                if ''.join(sorted(i)) not in mydict:
                    mydict[''.join(sorted(i))]=1
                else:
                    mydict[''.join(sorted(i))]+=1
    total=[]
    for menu,knt in mydict.items():
        total.append([menu,knt])
    total.sort(key=lambda x:[len(x[0]),-x[1]])
    box=[]
    start=0
    for idx,i in enumerate(total):
        if idx==0:
            k=course[start]
            maxsize=i[1]
        if len(i[0])>k:
            start+=1
            k=course[start]
            maxsize=i[1]
        if i[1]==maxsize and maxsize>1:
            box.append(i[0])
        else:
            pass
    answer=sorted(box)
    return answer