def solution(n): #피보나치 수열 
    a, b = 1, 2
    if n == 1:
        return 1
    for i in range(2,n):
        a, b = b, a+b
    return b % 1234567
