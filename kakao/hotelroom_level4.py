#효율성문제 :
#방을 찾는데 시간이 오래걸리는것인가?
#삽입하는데 시간이 오래 걸리는 것인가?(append하는 시간복잡도 O(1), insert하는 시간복잡도 O(N))
def solution(k, room_number):
    answer = []#[-1 for _ in range(len(room_number))]
    room_dict = {}
    # for i, v in enumerate(room_number):
    #     while True:
    #         if v in room_dict.values():
    #             v += 1
    #         else:
    #             room_dict[i] = v
    #             break
    
    # for i in range(len(room_number)):
    #     answer.append(room_dict[i])
    for num in room_number:
        number = room_dict.get(num, False)
        print(f"{num}\t number: {number}, dict: {room_dict}")
        #number가 False면 값이 없다는 뜻이므로 방배정이 아직 안됬다는 뜻이다. 그러나 방번호가 나오게 되면 이미 배정이 되어있으므로 다음 액션을 취해야함.
        if number :
            temp = [num]
            print(temp)
            while True:
                index = number
                number = room_dict.get(number, False)
                if not number:
                    answer.append(index)
                    room_dict[num] = index + 1
                    for i in temp:
                        room_dict[i] = index + 1
                    break   
                temp.append(number)
        else:
            answer.append(num)
            room_dict[num] = num + 1
    return answer


if __name__ == "__main__":
    k = 10	
    room_number = [1,3,4,1,3,1]

    print(solution(k, room_number))