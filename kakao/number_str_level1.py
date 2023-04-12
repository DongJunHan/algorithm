def solution(s):
    answer = s
    num_dict = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    # num = {"0":0, "1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    # temp = ""
    # for i in range(len(s)):
    #     if s[i] in num.keys():
    #         answer += s[i]
    #     else:
    #         temp += s[i]
    #         if temp in num_dict.keys():
    #             answer += num_dict[temp]
    #             temp = ""
    """ 답안. """
    for key, value in num_dict.items():
        answer = answer.replace(key, value)
    return int(answer)

if __name__ == "__main__":
    # s = "one4seveneight"
    # s = "23four5six7"
    s = "2three45sixseven"
    print(solution(s))