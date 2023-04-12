from math import ceil
def solution(fees, records):
    answer = []
    length = len(records)
    dictionary = {}
    total_minute = {}
    car_list = []
    for record in records:
        record_arr = record.split()
        if record_arr[1] not in car_list:
            car_list.append(record_arr[1])
        if record_arr[1] not in dictionary.keys():
            dictionary[record_arr[1]] = record_arr
        else:
            in_time = dictionary[record_arr[1]][0].split(":")
            out_time = record_arr[0].split(":")
            total_time = (int(out_time[0]) - int(in_time[0])) * 60 + (int(out_time[1]) - int(in_time[1]))
            dictionary.pop(record_arr[1])
            if record_arr[1] in total_minute.keys():
                total_minute[record_arr[1]] += total_time
            else:
                total_minute[record_arr[1]] = total_time
    if dictionary is not None:
        for key in dictionary.keys():
            in_time = dictionary[key][0].split(":")
            total_time = (23 - int(in_time[0])) * 60 + (59 - int(in_time[1]))
            if dictionary[key][1] in total_minute.keys():
                total_minute[dictionary[key][1]] += total_time
            else:
                total_minute[dictionary[key][1]] = total_time
    car_list.sort()
    for c in  car_list:
        remain_fee = 0
        basic_fee = fees[1]
        basic = total_minute[c] - fees[0]
        if basic > 0:
            remain_fee =  ceil((total_minute[c] - fees[0]) / fees[2]) * fees[3]
        answer.append(remain_fee + basic_fee)

    return answer

if __name__ == "__main__":
    fees = [180, 5000, 10, 600]
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    print(solution(fees, records))