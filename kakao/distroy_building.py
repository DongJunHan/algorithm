def solution(board:list, skill:list):
    """
        누적합으로 풀어야함.
        1. 빈 배열을 만드는데 기존의 board보다 행,열 모두 +1 크기만큼의 배열을 만든다.
        2. 누적합을 하기전에 좌표로 체크한다. (x1,y1) = damage, (x1,y2+1) = -damage, (x2+1, y1) = -damage, (x2+1, y2+1) = damage
        3. 누적합 수행
        4. borad와 더함.
    """
    length = len(skill)
    answer = 0
    m = len(board[0]) + 1
    arr = [[0] * m for _ in range(len(board)+1)]
    for i in range(length):
        if skill[i][0] == 1:
            skill[i][5] *= -1
        damage = skill[i][5]
        arr[skill[i][1]][skill[i][2]] += damage
        arr[skill[i][1]][skill[i][4] + 1] += (damage * -1)
        arr[skill[i][3] + 1][skill[i][4] + 1] += damage
        arr[skill[i][3] + 1][skill[i][2]] += (damage * -1)
    for i in range(len(arr) + (len(arr[0]) - len(arr))):
        temp = 0
        for j in range(len(arr[0]) + (len(arr) - len(arr[0]))):
            arr[j][i] += temp
            temp = arr[j][i]
    print(f"arr: {arr}")
    for i in range(len(arr)):
        temp = 0
        for j in range(len(arr[0])):
            arr[i][j] += temp
            temp = arr[i][j]
    print(f"arr: {arr}")

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += arr[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer




if __name__ == "__main__":
    # board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
    board = [[1,2,3],[4,5,6],[7,8,9]]
    skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
    # skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
    print(solution(board, skill))