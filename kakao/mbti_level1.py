def solution(servey:list, choices:list):
    # indicate = {"R":1, "T":1,"C":2,"F":2,"J":3,"M":3,"A":4,"N":4}
    answer = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    score = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    length = len(servey)
    indicate = ""
    for i in range(length):
        one = servey[i][0]
        two = servey[i][1]
        if choices == 0:
            continue
        elif choices[i] >= 1 and choices[i] < 4:
            score[one] += answer[choices[i]]
        elif choices[i] > 4 and choices[i] <= 7:
            score[two] += answer[choices[i]]
    
    if score["R"] >= score["T"]:
        indicate += "R"
    else:
        indicate += "T"
    
    if score["C"] >= score["F"]:
        indicate += "C"
    else:
        indicate += "F"
    
    if score["J"] >= score["M"]:
        indicate += "J"
    else:
        indicate += "M"
    
    if score["A"] >= score["N"]:
        indicate += "A"
    else:
        indicate += "N"
    return indicate

if __name__ == "__main__":
    # servey = ["AN", "CF", "MJ", "RT", "NA"]
    servey = ["TR", "RT", "TR"]
    # choices = [5, 3, 2, 7, 5]
    choices = [7, 1, 3]
    print(solution(servey, choices))