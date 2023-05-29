def solution(n):
    answer = 0
    cnt=1
    mok=n//2
    num1=2
    num2=1
    while(cnt<=mok):
        if cnt==1:
            answer=3
        else:
            answer=num1*4+num2*3
            num1=num1*3+num2*2
            num2=answer-num1        
        cnt+=1
    return answer%1000000007