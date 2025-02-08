
import sys
import copy

def solution(chess: list)->int:
    N = len(chess)
    M = len(chess[0])
    
    cut_N = 8
    cut_M = 8
    
    result = 999999
    for i in range(N):
        for j in range(M):
            if i + cut_N > N or j + cut_M > M:
                continue
            
            cut_chess =  [row[j:j+8] for row in chess[i:i+8]]
            change_count = count_change(cut_chess)
            
            if change_count < result:
                result = change_count
    
    return result
            

def count_change(chess: list)->int:
    min_c = []
    
    case_2 = ["W", "B"]
    for color in case_2:
        temp = copy.deepcopy(chess)
        r = 0
        if temp[0][0] != color:
            r += 1
        temp[0][0] = color
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                if i == 0 and j == 0:
                    continue
                
                if j == 0:
                    if temp[i][j] == temp[i-1][j]:
                        temp[i][j] = "W" if temp[i-1][j] == "B" else "B"
                        r += 1
                else:
                    if temp[i][j] == temp[i][j-1]:
                        temp[i][j] = "W" if temp[i][j-1] == "B" else "B"
                        r += 1


        min_c.append(r)
    
    return min(min_c)
            

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    chess = [list(sys.stdin.readline().strip()) for _ in range(N)]
    ret = solution(chess=chess)
    
    print(ret)
