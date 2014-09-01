
def merge_sort(left_array, right_array):

    i = 0
    j = 0
    sorted_array = []
    while i < len(left_array) or j < len(right_array):
        if (i == len(left_array)):
            sorted_array.append(right_array[j])
            j +=1
        elif (j == len(right_array)):
            sorted_array.append(left_array[i])
            i +=1
        elif left_array[i] <= right_array[j]:
            sorted_array.append(left_array[i])
            i +=1
        else:
            #right_array[j] <= left_array[i]
            sorted_array.append(right_array[j])
            j +=1

    return sorted_array

print merge_sort([0,4,8,9], [2,5,7,1])

def split_and_merge(array):
    middle_index = len(array)//2
    left_array = []
    right_array = []

    if len(array) < 2:
        return array
    else:
        for i in range(0, middle_index):
            left_array.append(array[i])
        for j in range(middle_index,len(array)):
            right_array.append(array[j])

    sorted_left_array = split_and_merge(left_array)
    sorted_right_array = split_and_merge(right_array)

    return merge_sort(sorted_left_array, sorted_right_array)

array = [1,4,6,8,9,7,2,3]
print split_and_merge(array)


