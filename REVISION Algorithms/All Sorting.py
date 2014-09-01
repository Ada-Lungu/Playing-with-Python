__author__ = 'ada'

# 7 min
def bubble_sorting(list):

    sorted = False
    left_margin = 0
    right_margin = len(list)

    while not sorted:
        sorted = True
        for elem_position in range(left_margin, right_margin-1):
            if list[elem_position] > list[elem_position+1]:
                list[elem_position], list[elem_position+1] = list[elem_position+1], list[elem_position]
                sorted = False
        right_margin -= 1

        for elem_position in range(right_margin-1, left_margin-1, -1):
            if list[elem_position] > list[elem_position+1]:
                list[elem_position], list[elem_position+1] = list[elem_position+1], list[elem_position]
                sorted = False
        left_margin += 1

    return list

print bubble_sorting([0,3,5,2,7,1,6,9,10])


# quick sort
def quick_sort(list, left_margin, right_margin):
    pivot_position = left_margin + (right_margin - left_margin)//2
    pivot = list[pivot_position]

    for elem_pos in range(left_margin, pivot_position):
        if list[elem_pos] > pivot:
            list.insert(pivot_position+1, list[elem_pos])
            del(list[elem_pos])
            pivot_position -= 1

    for elem_pos in range(pivot_position+1, right_margin+1):
        if list[elem_pos] < pivot:
            list.insert(pivot_position, list[elem_pos])
            del(list[elem_pos])
            pivot_position +=1

    quick_sort(list, left_margin, pivot_position-1)
    quick_sort(list, pivot_position+1, right_margin)

    return list

print quick_sort([0,3,5,2,7,1,6,9,10], 0, 8)
# 8 min



# Merge Sort

def sort_and_merge(left_array, right_array):
    i = 0
    j = 0
    merged_list = []

    while i < len(left_array) or j < len(right_array):
        if i == len(left_array):
            merged_list.append(right_array[j])
            j+=1
        elif j == len(right_array):
            merged_list.append(left_array[i])
            i+=1
        elif left_array[i] < right_array[j]:
            merged_list.append(left_array[i])
            i+=1
        else:
            merged_list.append(right_array[j])
            j+=1

    return merged_list


def split_and_merge(list):
    middle_index = len(list)//2
    left_array = []
    right_array = []

    if len(list) < 2:
        return list
    else:
        for elem_pos in range(0, middle_index):
            left_array.append(list[elem_pos])
        for elem_pos in range(middle_index, len(list)):
            right_array.append(list[elem_pos])

    left_splited = split_and_merge(left_array)
    right_splited = split_and_merge(right_array)

    return sort_and_merge(left_splited, right_splited)

print split_and_merge([0,3,5,2,7,1,6,9,10])

 #10 min
# 12 minutes





























