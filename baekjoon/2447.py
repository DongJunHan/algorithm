def solution(x:int=3):
    star_arr = [["*"]*x for _ in range(x)]
    tmp_x = x
    while tmp_x // 3 >= 1:
        tmp_x = tmp_x // 3
        for i in range(x):
            for j in range(x):
                if i // tmp_x % 3 == 1 and j // tmp_x % 3 == 1:
                    star_arr[i][j] = " "
    
    for i in star_arr:
        string = ""
        for j in i:
            string += j
        print(string)
        
if __name__ == "__main__":
    x = input()
    solution(int(x))