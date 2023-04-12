def solution(board, moves):
    answer = 0
    length = len(moves)
    b_len = len(board)
    prev = []
    keep = False
    for i in range(length):
        doll = -1
        move = moves[i] - 1
        for j in range(b_len):
            if board[j][move] != 0:
                doll = board[j][move]
                board[j][move] = 0
                break
        # 없는 경우
        if doll == -1:
            continue
        prev.append(doll)
        if len(prev) > 1:
            if prev[len(prev) - 1] == prev[len(prev) - 2]:
                answer += 2
                prev.pop()
                prev.pop()


    return answer

if __name__ == "__main__":
    """
        [0,0,0,0,0]
        [0,0,1,0,3]
        [0,2,5,0,1]
        [4,2,4,4,2]
        [3,5,1,3,1]
    """
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    # moves = [2,5,3,5,1,2,1,4]
    moves = [1,5,3,5,1,2,1,4]
    print(solution(board, moves))