from itertools import combinations
def solution(clothes):
    answer = 0
    # clothes_dic={}
    # for clothes_type in clothes:
    #     if clothes_type[1] not in clothes_dic:
    #         clothes_dic[clothes_type[1]]=[clothes_type[0]]
    #     else:
    #         clothes_dic[clothes_type[1]].append(clothes_type[0])
    # clothes_list=clothes_dic.keys()
    # can=[]
    # for i in range(1,len(clothes_list)+1):
    #     for j in list(combinations(clothes_list, i)):
    #         plus=1
    #         for k in j:
    #             plus*=len(clothes_dic[k])
    #         answer+=plus
    clothes_dic={}
    total=1
    for i in clothes:
        if i[1] not in clothes_dic:
            clothes_dic[i[1]]=1
        else:
            clothes_dic[i[1]]+=1
    for k in clothes_dic.values():
        total*=(k+1)
    return total-1