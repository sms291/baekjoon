def solution(number, limit, power):
    answer = 0
    warrier=[]
    for i in range(1,number+1):
        cnt=0
        for k in range(1,i+1):
            if i%k==0 and (i/k)>k:
                cnt+=2
            elif i%k==0 and (i/k)==k:
                cnt+=1
                break
            elif (i/k)<k:
                break
                
        warrier.append(cnt)
    for i in warrier:
        if i<=limit:    
            answer+=i
        else:
            answer+=power
        
    return answer