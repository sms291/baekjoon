def solution(genres, plays):
    answer = []
    gen_dic={}
    for idx,i in enumerate(genres):
        if i not in gen_dic:
            gen_dic[i]=plays[idx]
        else:
            gen_dic[i]+=plays[idx]
    total=[[p,g]for g,p in gen_dic.items()]
    total=sorted(total,reverse=True)
    #print(total)
    total_dic={}
    for idx,i in enumerate(total):
        total_dic[i[1]]=idx
    all=[[total_dic[g],p,idx]for (idx,g),p in zip(enumerate(genres),plays)]
    new=sorted(all,key=lambda x:[x[0],-x[1]])
    #print(new)
    cnt_dic={}
    for i in new:
        if i[0] not in cnt_dic:
            cnt_dic[i[0]]=1
            answer.append(i[2])
        else:
            if cnt_dic[i[0]]==2:
                continue
            else:
                cnt_dic[i[0]]+=1
                answer.append(i[2])
    
    return answer