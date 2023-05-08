N=int(input())
N_list=list(map(int,input().split()))

M=int(input())
M_list=list(map(int,input().split()))

number_dic={}
for i in N_list:
    if i not in number_dic:
        number_dic[i]=1
    else:
        number_dic[i]+=1
N_list.sort()
total=[]
#print(M_list)
for k in M_list:
    cnt=0
    left=0
    right=len(N_list)-1
    while(left<=right):
        mid=(left+right)//2
        if N_list[mid]==k:
            total.append(str(number_dic[k]))
            cnt=1
            break
        elif N_list[mid]>k:
            right=mid-1
        else:
            left=mid+1
    if cnt==0:
        total.append(str(0))
print(' '.join(total))