def solution(numbers):
    answer = ''
    numbers = [str(i) for i in numbers]
    l = len(numbers)
    #numbers의 원소는 0 이상 1,000 이하입니다. 라는 조건에 의해서 원소는 세 자리내에서 처리
    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = "".join(numbers)
    return str(int(answer))

if __name__ == "__main__":
    # numbers = [3, 30, 34, 5, 9]
    numbers = [0,0]
    ret = solution(numbers)
    print(f"ret={ret}")