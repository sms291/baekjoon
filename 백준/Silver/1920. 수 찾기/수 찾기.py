N=int(input())
N_list=list(map(int,input().split()))
N_list=sorted(N_list)
M=int(input())
M_list=list(map(int,input().split()))
for k in M_list:
    cnt=0
    left=0
    right=len(N_list)-1
    while(left<=right):
        mid=(left+right)//2
        if N_list[mid]==k:
            print(1)
            cnt=1
            break
        elif N_list[mid]>k:
            right=mid-1
        else:
            left=mid+1
    if cnt==0:
        print(0)
            