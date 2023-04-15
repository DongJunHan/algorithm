#https://school.programmers.co.kr/learn/courses/30/lessons/178871
def solution(players, callings):
    answer = []
    map_runner = {players[r]:r for r in range(len(players))}
    map_index = {r:players[r] for r in range(len(players))}
    for call in callings:
        i = map_runner[call]
        changer = map_index[i - 1]
        map_runner[changer] += 1
        map_runner[call] -= 1
        map_index[i - 1] = call
        map_index[i] = changer
    map_runner = sorted(map_runner.items(),key=lambda x:x[1])
    for i in map_runner:
        answer.append(i[0])
    return answer


if __name__ == "__main__":
    players = ["mumu", "soe", "poe", "kai", "mine"]
    callings = ["kai", "kai", "mine", "mine"]
    ret = solution(players, callings)
    print(f"ret={ret}")
    #["mumu", "kai", "mine", "soe", "poe"]