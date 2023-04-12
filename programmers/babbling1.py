def solution(babbling):
    """
    문제:머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 
    네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 
    문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.
        핵심. replace함수를 사용해서 처리.
    """
    answer = 0
    flag = False
    arr = ["aya", "ye", "woo", "ma" ]
    for i in babbling:
        check_arr = [False for n in range(len(i))]
        for j in arr:
            if j not in i:
                continue
            i = i.replace(j, " ")
        if len(i.strip()) == 0:
            answer += 1

    return answer

if __name__ == "__main__":
    # babbling = ["aya", "yee", "u", "maa", "wyeoo"]
    babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
    print(f"answer = {solution(babbling)}")
