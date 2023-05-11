def solution(n):
# 답안 작성 부분 ===============
    
    answer=0
    for i in range(1,n+1):
        knt=0
        if i!=1:
            
            for k in range(1,i+1):
                if i%k==0:
                    if (k==1) or (k==i):
                        pass
                    else:
                        knt=1
                        break
        if knt==0 and i!=1:
            answer+=1

    # answer=cnt

# ==============================
    return answer