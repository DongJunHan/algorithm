import sys

def solution(goal_number: int, second_values: list[int]) -> int:
    nearest_number = 0

    for i, v in enumerate(second_values, start=0):
        for j in range(i+1, len(second_values)):
            v1 = second_values[j]
            for k in second_values[j+1:]:
                near_number = v + v1 + k
                if goal_number == near_number:
                    return near_number
                elif nearest_number < near_number < goal_number:
                    nearest_number = near_number

    return nearest_number


if __name__ == "__main__":
    loop_num, goal_number = map(int, sys.stdin.readline().strip().split())
    second_values = list(map(int, sys.stdin.readline().strip().split()))
    
    answer = solution(goal_number=goal_number, second_values=second_values)
    print(answer)

 
