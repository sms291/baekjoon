def solution(str1, str2):
    answer = 0
    str1=str1.lower()
    str2=str2.lower()
    str1_dic={}
    str2_dic={} 
    for i in range(len(str1)-1):
        if str1[i:i+2] not in str1_dic and str1[i].isalpha() and str1[i+1].isalpha():
            str1_dic[str1[i:i+2]]=1
        elif str1[i:i+2] in str1_dic and str1[i].isalpha() and str1[i+1].isalpha():
            str1_dic[str1[i:i+2]]+=1
    for i in range(len(str2)-1):
        if str2[i:i+2] not in str2_dic and str2[i].isalpha() and str2[i+1].isalpha():
            str2_dic[str2[i:i+2]]=1
        elif str2[i:i+2] in str2_dic and str2[i].isalpha() and str2[i+1].isalpha():
            str2_dic[str2[i:i+2]]+=1
            
            
    #print(str1_dic)
    #print(str2_dic)
    
    num1=str1_dic.keys()
    num2=str2_dic.keys()
    total=0
    cnt=0
    same=[]
    for k in num1:
        if k in num2:
            same.append(k)
    for i in num1:
        if i not in same:
            total+=str1_dic[i]
    for i in num2:
        if i not in same:
            total+=str2_dic[i]        
    for k in num1:
        if k in num2:
            if str1_dic[k]<=str2_dic[k]:
                cnt+=str1_dic[k]
                total+=str2_dic[k]
            else:
                cnt+=str2_dic[k]
                total+=str1_dic[k]
    #print(cnt)
    if len(num1)+len(num2)==0:
        answer=65536
    else:
        answer=int((cnt/(total))*65536)
        pass
    return answer