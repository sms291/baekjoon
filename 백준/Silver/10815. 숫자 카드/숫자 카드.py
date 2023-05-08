N=int(input())
N_list=list(map(int,input().split()))
N_list.sort()
M=int(input())
M_list=list(map(int,input().split()))
# print(N_list)
# print(M_list)
for i in M_list:
    left=0
    right=len(N_list)-1
    cnt=0
    while(left<=right):
        mid=(left+right)//2
        
        if N_list[mid]==i:
            print(1,end=' ')
            cnt=1
            break
        elif N_list[mid]>i:
            right=mid-1
        else:
            left=mid+1
    if cnt==0:
        print(0,end=' ')