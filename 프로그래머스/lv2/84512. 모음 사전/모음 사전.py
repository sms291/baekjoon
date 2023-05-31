def solution(word):
    answer = 0
    word_vec=[]
    for i in ['A', 'E', 'I', 'O', 'U']:
        if i not in word_vec:
            word_vec.append(i)
        for j in ['A', 'E', 'I', 'O', 'U']:
            if i+j not in word_vec:
                word_vec.append(i+j)
            for k in ['A', 'E', 'I', 'O', 'U']:
                if i+j+k not in word_vec:
                    word_vec.append(i+j+k)
                for u in ['A', 'E', 'I', 'O', 'U']:
                    if i+j+k+u not in word_vec:
                        word_vec.append(i+j+k+u)
                    for t in ['A', 'E', 'I', 'O', 'U']:
                        if i+j+k+u+t not in word_vec:
                            word_vec.append(i+j+k+u+t)
    word_vec.sort()
    answer=word_vec.index(word)+1
    return answer