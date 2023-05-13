def solution(s):
    answer = []
    s=s[1:-1]
    number_dic={}
    number=''
    total=[]
    for i in s:        
        if i not in ['{','}',',']:
            number+=i
        else:
            if number!='':
                if number not in number_dic:
                    number_dic[number]=1
                else:
                    number_dic[number]+=1
            number=''
    for number,cnt in number_dic.items():
        total.append([cnt,int(number)])
    total=sorted(total,reverse=True)
    for k in total:
        answer.append(k[1])

    return answer