import re
def solution(s):
    answer = ''
    arr = s.split(" ")
    com = re.compile("[0-9]")
    for i in range(len(arr)):
        if arr[i] == "":
            continue
        arr[i] = arr[i].lower()
        if len(com.findall(arr[i][0])) == 0:
            arr[i] = arr[i][0].upper() + arr[i][1:]
    answer = " ".join(arr)
    return answer


if __name__ == "__main__":
    s = "3people  unFollowed me"
    #s = "for the last week"
    ret = solution(s)
    print(f"ret={ret}")