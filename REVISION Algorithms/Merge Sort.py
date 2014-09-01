__author__ = 'ada'


# Variant 2 with i, j - indexes of the two lists: left and right lists

def sort_and_merge_indexes(left_array, right_array):
    left_array_index = 0
    right_array_index = 0
    merged_list = []

    while left_array_index < len(left_array) or right_array_index < len(right_array):
        if left_array_index == len(left_array):
            merged_list.append(right_array[right_array_index])
            right_array_index += 1

        elif right_array_index == len(right_array):
            merged_list.append(left_array[left_array_index])
            left_array_index += 1

        elif left_array[left_array_index] <= right_array[right_array_index]:
            merged_list.append(left_array[left_array_index])
            left_array_index += 1

        else:
            merged_list.append(right_array[right_array_index])
            right_array_index += 1

    return merged_list

print sort_and_merge_indexes([2,4,6,7],[1,3,8,9])
print sort_and_merge_indexes([0,4,8,9], [2,5,7,1])


def split_and_merge_indexes(list):
    middle_position = len(list)//2
    midd_elem = list[middle_position]
    left_array = []
    right_array = []

    if len(list) < 2:
        return list
    else:
        for elem_pos in range(0, middle_position):
            left_array.append(list[elem_pos])
        for elem_pos in range(middle_position, len(list)):
            right_array.append(list[elem_pos])

    left_splited = split_and_merge_indexes(left_array)
    right_splited = split_and_merge_indexes(right_array)

    return sort_and_merge_indexes(left_splited, right_splited)

print split_and_merge_indexes([2,4,6,8,3,1,11,9,7,10])



# merge_and_sort method
# split_and_merge method

def sort_and_merge(left_list, right_list):

    merged_list = []

    while len(left_list) > 0 and len(right_list) > 0:
        if len(left_list) == 0:
            for elem_pos in range(len(right_list)):
                merged_list.append(right_list[elem_pos]) # merged_list = merged_list + right_list
        if len(right_list) == 0:
            for elem_pos in range(len(left_list)):
                merged_list.append(len(left_list))

        for left_elem_pos in range(len(left_list)):
            for right_elem_pos in range(len(right_list)):
                if left_list[left_elem_pos] < right_list[right_elem_pos]:
                    merged_list.append(left_list[left_elem_pos])
                    del(left_list[left_elem_pos])

                if right_list[right_elem_pos] < left_list[left_elem_pos]:
                    merged_list.append(right_list[left_elem_pos])
                    del(right_list[right_elem_pos])

    return merged_list

print sort_and_merge([2,4,6,7],[1,3,8,9])


def split_and_merge(list):
    middle_list_pos = len(list)//2
    middle_elem = list[middle_list_pos]
    left_list = []
    right_list = []
    left_margin = 0
    right_margin = len(list)

    if len(list) > 1:
        for i in range(left_margin, middle_list_pos):
            left_list.append(list[i])
        for j in range(middle_list_pos, right_margin):
            right_list.append(list[j])

    left_splited_array = split_and_merge(left_list)
    right_splited_array = split_and_merge(right_list)

    return sort_and_merge(left_splited_array, right_splited_array)


print split_and_merge([2, 4, 7, 6, 0, 10, 19])
























