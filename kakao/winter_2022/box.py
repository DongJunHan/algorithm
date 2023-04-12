def solution(x, y, z):
    """
        x : start
        y : end
        z : count
    """
    sub = abs(x - y)
    if sub > z:
        return -1
    elif sub == 0:
        return x + (z // 2)
    else:
        if x > y:
            return x + ((z-sub)//2)
        else:
            return y + ((z - sub) // 2)




if __name__ == "__main__":
    x = 100000000
    y = 99999998
    z = 12
    print(solution(x, y, z))