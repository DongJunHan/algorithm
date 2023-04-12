def preorder(arr, column, row):
    find = arr[column][row]
    string = ""
    for i in range(len(arr)):
        if arr[i] in find:
            break
    preorder(arr, column+1, row)


if __name__ == "__main__":
    x = input()
    arr = [[0]*3 for _ in range(int(x))]
    for i in range(int(x)):
        put = input()
        sub_arr = put.split()
        for j in range(3):
            arr[i][j] = sub_arr[j]
      