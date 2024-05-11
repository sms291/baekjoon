import sys
A,B=map(int,input().split())
# K=[int(sys.stdin.readline()) for _ in range(A)]
K = list(map(int,input().split()))
start,end = 1,sum(K)
while start<=end:
    mid = (start + end) // 2 #중간 위치
    lines = 0 #랜선 수
    for i in K:
        if i>mid:
            lines += i - mid #분할 된 랜선 수
    if lines >= B: #랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid -1   
    

print(end)