def solution(numbers, hand):
    answer = ''
    left = [1,4,7]
    right = [3,6,9]
    phone_num = {1:(3,0),2:(3,1),3:(3,2),4:(2,0),5:(2,1),6:(2,2),7:(1,0),8:(1,1),9:(1,2),"*":(0,0),0:(0,1),"#":(0,2)}
    save_left = -1
    save_right = -1
    for num in numbers:
        if num in left:
            answer += "L"
            save_left = num
            print(f"@left: {save_left}, right: {save_right}, num: {num}")
            continue
        elif save_left != -1:
            left_range = abs(phone_num[num][0] - phone_num[save_left][0]) + abs(phone_num[num][1] - phone_num[save_left][1])
        else:
            left_range = abs(phone_num[num][0] - phone_num["*"][0]) + abs(phone_num[num][1] - phone_num["*"][1])
        
        if num in right:
            answer += "R"
            save_right = num
            print(f"left: {save_left}, right: {save_right}, num: {num}")
            continue
        elif save_right != -1:
            right_range = abs(phone_num[num][0] - phone_num[save_right][0]) + abs(phone_num[num][1] - phone_num[save_right][1])
        else:
            right_range = abs(phone_num[num][0] - phone_num["#"][0]) + abs(phone_num[num][1] - phone_num["#"][1])
        print(f"lr: {left_range}, rr: {right_range}, left: {save_left}, right: {save_right}, current_num: {num}")
        if left_range == right_range:
            answer += hand[0].upper()
            if hand == "right":
                save_right = num
            else:
                save_left = num
        elif left_range < right_range:
            answer += "L"
            save_left = num
        else:
            answer += "R"
            save_right = num

    return answer


if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = "right"
    print(solution(numbers, hand))