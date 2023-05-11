def solution(n):
    answer = 0
    a=[False,False]+[True]*(n-1)
    prime=[]

    for i in range(2,n+1):
        if a[i]:
            prime.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    answer=len(prime)
    return answer