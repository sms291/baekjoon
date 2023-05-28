s=input()
su=''
total=0
switch=1
for idx,i in enumerate(s):
    #print(total)
    if i not in ['+','-']:
        su+=i
    else:
        if i=='+':
            if switch==1:
                total+=int(su)
                su=''
            else:
                total-=int(su)
                su=''
        else:
            if switch==1:
                switch=0
                total+=int(su)
                su=''           
            else:
                total-=int(su)
                su=''   
    if idx==len(s)-1 and switch==0:
        total-=int(su)            
    elif idx==len(s)-1 and switch==1:
        total+=int(su)
print(total)