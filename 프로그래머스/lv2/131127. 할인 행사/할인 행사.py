def solution(want, number, discount):
    answer = 0
    ex={}
    for food,many in zip(want,number):
        ex[food]=many   
    total={}
    k=0
    while(1):
        if k==0:
            for i in range(10):
                if discount[i] not in total:
                    total[discount[i]]=1
                else:
                    total[discount[i]]+=1
        else:
            total[discount[k-1]]-=1
            
            if discount[9+k] not in total:
                total[discount[9+k]]=1
            else:
                total[discount[9+k]]+=1
            if total[discount[k-1]]==0:
                del total[discount[k-1]]
        bad=0
        for i in want:
            if (i in total):
                if total[i]==ex[i]:
                    pass
                else:
                    bad=1
                    break
            else:
                bad=1
                break
        if bad==0:
            answer+=1
        
        if k==len(discount)-10:
            break
        k+=1
    return answer
    #치킨 0
    #사과 2
    #바나나 3
    #쌀 2
    #돼지고기 2
    #냄비 1