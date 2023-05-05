def solution(arr):
    number1={}
    for num in arr:
        number2={}
        while(1):
            cnt=0
            for i in range(1,num+1):
                if i!=1 and num%i==0 and (i not in number2):
                    number2[i]=1
                    num=num//i
                    cnt=1
                    break
                elif i!=1 and num%i==0 and (i in number2):
                    number2[i]+=1
                    num=num//i
                    cnt=1
                    break
            if cnt==0:
                break
        for i in number2.keys():
            if i not in number1:
                number1[i]=number2[i]
            else:
                if number1[i]<number2[i]:
                    number1[i]=number2[i]
    total=1
    for j in number1:
        total*=j**number1[j]
    
    return total