# def solution(s):
#     answer = []
#     s=s[1:-1]
#     number_dic={}
#     number=''
#     total=[]
#     for i in s:        
#         if i not in ['{','}',',']:
#             number+=i
#         else:
#             if number!='':
#                 if number not in number_dic:
#                     number_dic[number]=1
#                 else:
#                     number_dic[number]+=1
#             number=''
#     for number,cnt in number_dic.items():
#         total.append([cnt,int(number)])
#     total=sorted(total,reverse=True)
#     for k in total:
#         answer.append(k[1])

#     return answer
def solution(s):
# 답안 작성 부분 ===============
    answer = []
    dic={}
    su=''
    for i in s:  
        if i.isalnum():
            su+=i
        else:
            if not su:
                pass
            else:
                if su not in dic:
                    dic[su]=1
                else:
                    dic[su]+=1
            su=''
            total=[]
    for k,v in dic.items():
        total.append([v,int(k)])
    answer=[int(k[1]) for k in sorted(total,key=lambda x: -x[0])]
# ==============================
    return answer