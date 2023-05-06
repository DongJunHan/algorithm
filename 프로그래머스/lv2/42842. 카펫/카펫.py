def solution(brown, yellow):
    answer = []
    
    for i in range(3, 3000):
        for j in range(3,3000):
            if (i - 2) * (j - 2) == yellow and i * j == (brown+yellow):
                return [max(i,j), min(i,j)]
    
    return answer