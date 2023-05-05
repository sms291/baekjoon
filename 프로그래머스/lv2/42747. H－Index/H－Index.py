def solution(citations):
    maximum=0
    dic={}
    for i in range(max(citations)+1):
        dic[i]=0

    for i in citations:
        for k in range(i+1):
            dic[k]+=1

    for i in dic.keys():
        if i<=dic[i]:
            maximum=i
    #print(maximum)
    return maximum