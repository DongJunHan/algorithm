def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer

if __name__ == "__main__":
    A = [1,2]
    B = [3,4]
    ret = solution(A, B)
    print(f"ret={ret}")
    