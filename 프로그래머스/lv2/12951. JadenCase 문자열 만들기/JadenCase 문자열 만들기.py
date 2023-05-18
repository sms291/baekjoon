import re
def solution(s):
    s_org=s
    s_ch=re.sub('[^\s]+','!',s_org)
    s=s.strip()
    s=re.sub("[\s]+",' ',s)

    t=s.split(' ')
    word=[]
    for i in t:

        if i[0].isalpha()==True:
            word.append(i[0].upper()+i[1:].lower())
        else:
            word.append(i.lower())
    answer=''
    cnt=0
    for i in s_ch:

        if i!=' ':
            answer+=word[cnt]
            cnt+=1
        else:
            answer+=' '
    return answer