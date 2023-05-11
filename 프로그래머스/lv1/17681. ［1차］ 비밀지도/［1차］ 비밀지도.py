def solution(n, arr1,arr2):
# 답안 작성 부분 ===============
  
  answer=[]
  for i in range(n):
   
    a1=bin(arr1[i])[2:].zfill(n)
    a2=bin(arr2[i])[2:].zfill(n)
    hang=''
    # print(a1)
    # print(a2)
    for idx,k in enumerate(a1):
      # print(idx)
      # print(k)
      if k=='1' or a2[idx]=='1':
        hang+='#'
      else:
        hang+=' '
    answer.append(hang)
        


# ==============================
  return answer