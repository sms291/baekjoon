def solution(n,A,B):
    answer=1
    if A>B:
        A,B=B,A
    while(1):
        if (((A//2)+1)==B//2) and(A+1==B):
            break
        if A%2==0:
            A=A//2
        else:
            A=(A//2)+1
        if B%2==0:
            B=B//2
        else:
            B=(B//2)+1    
        answer+=1


    return answer