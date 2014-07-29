
"""def minimum_num(num_list):

    min_num = num_list[0]

    for each_num in range(0,len(num_list)-1):
        each_num_is_min = True
        for next_num in range(1, len(num_list)):
            if each_num > next_num:
                each_num_is_min = False
            else:
                continue
        if each_num_is_min:
            min_num = i
    return min_num"""


# Version 2 - linear solution

def minimum_num(num_list):

    minsofar = num_list[0]
    for i in num_list:
        if i < minsofar:
            minsofar = i
    return minsofar

print minimum_num([3,5,6,8,1])













