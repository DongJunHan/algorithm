#https://school.programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    answer = ''
    arr = s.split(" ")
    # a = list(map(int,s.split())) #str 타입 원소를 다른 타입으로 바꾸는 방법
    arr.sort(key=lambda x:int(x))
    answer = arr[0] + " " + arr[len(arr)-1]
    return answer

if __name__ == "__main__":
    s = "1 2 3 4"
    ret = solution(s)
    print(f"ret={ret}")