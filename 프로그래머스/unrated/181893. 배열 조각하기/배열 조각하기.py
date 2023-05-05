def solution(arr, query):
    answer = []
    for idx,i in enumerate(query):
        if idx%2==0:
            arr=arr[:i+1]
        else:
            arr=arr[i:]
    answer=arr            
    return answer