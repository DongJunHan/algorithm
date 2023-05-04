import math
def solution(n, words):
    answer = []
    tmp = {words[0]:0}
    for i in range(1,len(words)):
        if words[i] in tmp.keys():
            answer.append((i % n) + 1)
            answer.append(math.ceil((i+1) / n))
            return answer
        if words[i][0] != words[i-1][len(words[i-1])-1]:
            answer.append((i % n) + 1)
            answer.append(math.ceil((i+1) / n))
            return answer
        tmp[words[i]] = 0
        
    return [0,0]