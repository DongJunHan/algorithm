def solution():
    a = input()
    a = int(a)
    count2 = 99999
    five = a // 5
    if five == 0:
        if a % 3 != 0:
            return -1
        else:
            return a // 3
    count = five
    if a % 3 == 0:
        count2 = a // 3
    for i in range(five,0,-1):
        if a - (5 * i) == 0:
            return count
        three = a - (5 * i)
        if three % 3 == 0:
            count += three // 3
            break
        count -= 1
    if count > 0 and count < count2:
        return count
    elif count2 != 99999:
        return count2
    return -1


if __name__ == "__main__":
    print(solution())