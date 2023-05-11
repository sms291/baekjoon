# def solution(name, yearning, photo):
#     answer = []
#     dict_={}
#     for n,y in zip(name,yearning):
#         if n not in dict_:
#             dict_[n]=y
        
    
#     for i in photo:
#         total=0
#         for k in i:
#             if k in dict_: 
#                 total+=dict_[k]
#         answer.append(total)
    
#     return answer
def solution(name, yearning, photo):
# 답안 작성 부분 ===============
    name_dic={}
    for naming,year in zip(name,yearning):
        if naming not in name_dic:
            name_dic[naming]=year 
    answer=[]
    for k in photo:
        total=0
        for photo_file in k:
            if photo_file in name_dic:
                total+=name_dic[photo_file]     
        answer.append(total)



# ==============================
    return answer