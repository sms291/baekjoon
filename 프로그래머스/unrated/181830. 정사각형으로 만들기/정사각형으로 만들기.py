def solution(arr):
    answer = []
    col=len(arr)
    raw=len(arr[0])
    if col==raw:
        answer=arr
    else:
        if col>raw:
            
            for i in range(col):
                
                answer.append(arr[i]+[0]*(col-raw))
            
        else:
            for i in range(col):
                answer.append(arr[i])
            for k in range(raw-col):
                answer.append([0]*raw)
    
    return answer