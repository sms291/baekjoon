def solution(n):
# 답안 작성 부분 ===============
  answer=0
  knt=1
  while(n>1 ):
    if knt==500:
      break
    if n%2==0:
      n=n//2
      answer+=1
    elif n%2!=0:
      n=(n*3)+1
      answer+=1
    knt+=1
    
      
  if n!=1:
      answer=-1
# ==============================
  return answer