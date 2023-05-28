def solution(n, s):
    answer = []
    mok=s//n
    nam=(s%n)
    if mok==0:
        answer=[-1]
    else:
        answer=[mok]*(n-nam)+[mok+1]*nam
        
    
    return answer