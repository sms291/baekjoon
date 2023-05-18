def solution(n):
    answer = 0
    mon=[0,1,2]
    a=1
    b=2
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        for i in range(3,n+1):
            a,b=b,a+b
    return b%1000000007