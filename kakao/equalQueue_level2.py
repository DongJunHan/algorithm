def solution(queue1:list, queue2:list):
    """
        1. 주어진 큐의 길이 범위가 300,000까지이기 때문에 매번 큐들의 합을 새로 처음부터 구할수는 없다.
        2. queue의 insert, pop을 매번 수행할 수 없다.
        3. 같은 합을 구하려면 절반값보다 큰 큐에서 요소를 빼서 절반값보다 작은 큐에 요소를 넣어주면 된다.
        *** 생각보다 sum() 함수에서 시간을 많이 뺐겼다. 오히려 append 삽입함수는 시간을 많이 뺐기지 않았다.
    """
    answer = -1
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    s = (sum1+sum2) // 2
    i, j, t = 0, 0, len(queue1)
    while i < t * 2 and j < t * 2 and sum1 != sum2:
        if sum1 < s:
            sum1 += queue2[j]
            sum2 -= queue2[j]
            queue1.append(queue2[j])
            j += 1
        else:
            sum2 += queue1[i]
            sum1 -= queue1[i]
            queue2.append(queue1[i])
            i += 1
    if sum1 == sum2:
        answer = i + j
    return answer


if __name__ == "__main__":

    queue1 = [3, 2, 7, 2]
    queue2 = [4, 6, 5, 1]
    # queue1 = [1,2,1,2]
    # queue2 = [1,10,1,2]
    # queue1 = [1,1]
    # queue2 = [1,5]
    print(solution(queue1, queue2))