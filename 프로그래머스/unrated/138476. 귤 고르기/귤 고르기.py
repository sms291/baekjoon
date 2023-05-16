def solution(k, tangerine):
    answer = 0
    dic={}
    for i in tangerine:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    song=[]
    for size,kind in dic.items():
        song.append([kind,size])
    song.sort(reverse=True)
    #print(song)
    total=0
    while(1):
        total+=song[answer][0]
        if k<=total:
            answer+=1
            break
        else:
            answer+=1
            
    return answer