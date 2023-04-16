def solution(m, n, startX, startY, balls):
    answer = []
    #벽에 부딪칠 위치 선정 중요해보임
    for ball in balls:
        cd1 = getDistance(startX, startY, ball[0], n+(n - ball[1]))
        cd2 = getDistance(startX, startY, m + (m - ball[0]), ball[1])
        cdmin = min(cd1,cd2)
        if startY != ball[1]:
            cd3 = getDistance(startX, startY, ball[0], 0 - (ball[1]))
            cdmin = min(cd1,cd2, cd3)
        else:
            cd3 = 0

        if startX != ball[0]:
            cd4 = getDistance(startX, startY, 0 - ball[0], (ball[1]))
            if cd3 == 0:
                cdmin = min(cd1,cd2,cd4)
            else:
                cdmin = min(cd1,cd2,cd3,cd4)
        answer.append(cdmin)
        
    return answer

def getDistance(startX, startY, x,y):
    # print(f"start: {startX}, {startY}, end: {x},{y}")
    dx = abs(startX - x) ** 2
    dy = abs(startY - y) ** 2
    return dx+dy
     

if __name__ == "__main__":
    m = 10
    n = 10
    startX = 3
    startY = 7
    balls = [[7, 7],[2, 7], [7, 3]]
    ret = solution(m, n, startX, startY, balls)
    print(f"ret={ret}")