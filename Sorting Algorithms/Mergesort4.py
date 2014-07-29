
def merge_sort_array(left_array, right_array):
    i = 0
    j = 0
    merged_array = []


    while i <= len(left_array) and j <= len(right_array): # NU AR trebui pus separat cazul cu == / cum poti zice aici doar < si apoi la next ==

        if i == len(left_array):
            merged_array.append(right_array[j])
            j+=1
        if j == len(right_array):
            merged_array.append(left_array[i]) # aici daca restul arrayului lui left/right nu e ordonat crescator, o sa mi-l puna asa???
            i+=1
        if left_array[i] <= right_array[j]:
            merged_array.append(left_array[i])
            i +=1
        if right_array[j] <= left_array[i]:
            merged_array.append(right_array[j])
            j +=1

    return merged_array


def split_and_merge(array):

    left_array = []
    right_array = []
    middle_index = len(array)//2

    if len(array) < 2:
        return array
    else:
    # de ce nu se poate direct if len(array) > 2:
        for i in range(0, middle_index):
            left_array.append(array[i])
        for j in range(middle_index, len(array)):
            right_array.append(array[j])

    left_sorted_array = split_and_merge(left_array)
    right_sorted_array = split_and_merge(right_array)

    return merge_sort_array(left_sorted_array, right_sorted_array)


left_array = [2, 5, 7, 9]
right_array = [1, 3, 7, 8, 11, 9]

print merge_sort_array(left_array, right_array)
print split_and_merge(right_array)








