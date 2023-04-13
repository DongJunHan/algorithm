#https://school.programmers.co.kr/learn/courses/30/lessons/42748?language=python3
def solution(array, commands):
    answer = []
    for command in commands:
        cut_arr = array[command[0]-1:command[1]]
        sort_arr = sorted(cut_arr)
        answer.append(sort_arr[command[2]-1])
    return answer

if __name__ == "__main__":
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    ret = solution(array, commands)
    print(f"ret={ret}")