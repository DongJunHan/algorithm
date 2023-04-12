from itertools import combinations_with_replacement as cwr
from collections import Counter

# def bfs(info, queue, n, i):
#     if n == 0:
#         return info, queue
#     if i > len(queue) - 1:
#         return info, queue

#     print(f"n: {n}, info: {(info[i] + 1)}, n-f: {n - (info[i] + 1)},i : {i}")
#     if info[i] == 0:
#         queue[i] = 1
#         info, queue = bfs(info, queue, n - 1, i + 1)
#     else:
#         if n - info[i] > 0:
#             queue[i] = info[i] + 1
#             print(f"queue: {queue}\tinfo: {info}\t n: {n},{n - (info[i] + 1)}, info: {info[i]}, {i}")
#             n = n - (info[i] + 1)
#             info[i] = 0
#             info, queue = bfs(info, queue, n , i + 1)
#         else:
#             info, queue = bfs(info, queue, n, i+1)
#     return info, queue

# def solution(n, info):
#     """
#         bfs(Breadth First Search)로 생각해보기
#     """
#     answer = []
#     #deque([(0, [0,0,0,0,0,0,0,0,0,0,0])]) 
#     # queue = [0 for _ in range(len(info))]
#     max_diff = 0
#     p = 10
#     length = len(info)
#     # for i in range(length):
#     #     if info[i] > 0:
#     #         score += 1 * (p - i)
#     for i in range(length):
#         tmp_info = info.copy()
#         tmp_queue = [0 for _ in range(len(info))]
#         sum1 = 0
#         score = 0
#         tmp_info, tmp_queue = bfs(tmp_info, tmp_queue, n, i)
#         for k in range(length):
#             if tmp_info[k] > 0:
#                 score += 1 * (p - k)
#         for k in range(length):
#             if tmp_queue[k] > 0:
#                 sum1 += (1 * (p - k))
#         print(f"score: {score}, sum: {sum1}, diff: {sum1 - score}")
#         print("========")
#         if max_diff < (sum1 - score):
#             max_diff = max(max_diff, (sum1 - score))
#             answer = tmp_queue.copy()
    
#     if len(answer) == 0:
#         answer =  -1

#     #while queue:
#         #force, array = queue.popleft()
#         #print(f"f : {force}, array: {array}")
#     return answer
def solution(n, info):
    answer = []
    info = info[::-1]
    max_n = -1
    length = len(info)
    z = 0
    for c in cwr(range(0, length), n) :
        z += 1
        ryan = 0
        apeach = 0
        tmp_ans = [0 for _ in range(length)]
        c = Counter(c)
        for i in range(0, length) :
            if info[i] < c[i] : # 개수가 더 많으면 라이언이 승
                ryan += i
            elif info[i] != 0 : # 아니면 어피치가 승
                apeach += i

            tmp_ans[i] = c[i]
        if ryan > apeach :
            diff = ryan - apeach
            if max_n < diff :
                max_n = diff
                answer = tmp_ans
    print(z)
    if answer :
        return answer[::-1]
    else :
        return [max_n]
if __name__ == "__main__":
    n = 9
    info = [0,0,1,2,0,1,1,1,1,1,1]
    # info = [2,1,1,1,0,0,0,0,0,0,0]
    print(solution(n, info))