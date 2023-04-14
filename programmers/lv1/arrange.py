#https://school.programmers.co.kr/learn/courses/30/lessons/161990
def solution(wallpaper):
    answer = []
    start = False
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                if start == False:
                    answer.append(i)
                    answer.append(j)
                    start = True
                elif len(answer) < 3:
                    answer.append(i)
                    answer.append(j)
                else:
                    #start쪽보다 작은가?
                    if j < answer[1]:
                        answer[1] = j
                    #end쪽 좌표보다 큰가?
                    if j > answer[3]:
                        answer[3] = j
                    if i > answer[2]:
                        answer[2] = i
    if len(answer) > 2:
        answer[2] = answer[2] + 1
        answer[3] = answer[3] + 1
    else:
        answer.append(answer[0] + 1)
        answer.append(answer[1] + 1)
    return answer