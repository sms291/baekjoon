def solution(arr):
    answer = []
    cnt=0
    while(1):
        if len(arr)>2**cnt:
            cnt+=1
        else:
            break
    answer=arr+((2**cnt)-len(arr))*[0]

    return answer