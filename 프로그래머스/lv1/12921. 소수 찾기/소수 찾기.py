def solution(n):
    answer = 0
    sosu=[0,0]+[1]*(n-1)
    primes=[]
    for i in range(2,n+1):
        if sosu[i]==1:
            primes.append(i)
            for k in range(2*i,n+1,i):
                sosu[k]=0
    answer=len(primes)
            
    return answer