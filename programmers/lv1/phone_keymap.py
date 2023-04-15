#https://school.programmers.co.kr/learn/courses/30/lessons/160586
def solution(keymap, targets):
    answer = []
    alphabet = {i:101 for i in "ABCDEFGHIJKMLNOPQRSTUVWXYZ"}
    for key in keymap:
        for i in range(len(key)):
            if alphabet[key[i]] > (i+1):
                alphabet[key[i]] = (i+1)
            
            
    for target in targets:
        ret = 0
        for i in range(len(target)):
            if alphabet[target[i]] == 101:
                ret = -1
                break
            ret += alphabet[target[i]]
        answer.append(ret)
    return answer


if __name__ == "__main__":
    # keymap = ["ABACD", "BCEFD"]
    # targets = ["ABCD","AABB"]
    keymap = ["ABCEF"]
    targets = ["ABCDE"]
    ret = solution(keymap, targets)
    print(f"ret={ret}")