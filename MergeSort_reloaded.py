
# create the merge_sort - merges 2 arrays and sorts them in one array
def merge_sort(left_array, right_array):
    my_array = []
    i = 0 # indexul elementelor lui left_array
    j = 0 # indexul lui right_array
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j] or j == len(right_array):
            my_array.append(left_array[i])
            i +=1
        elif left_array[i] == right_array[j]:
            my_array.append(left_array[i])
            i +=1
            j+=1
        elif right_array[j] < left_array[i] or i == len(left_array):
            my_array.append(right_array[j])
            j+=1

    return my_array


"""l_arr = [3,5,7,8,9]
r_arr = [1,2,4,7,9,10,2,11]
print merge_sort(l_arr, r_arr)"""


def split_and_merge(my_array):
    mid_index = len(my_array)//2
    left_array = []
    right_array = []

    if len(my_array)< 2: # when the array is composed of just one element
        return my_array
    else:
        for i in range(0, mid_index): # indexul in my_array
            left_array.append(my_array[i]) # formam left_arr ==> appenduim fiecare element de pe indexul i
        for i in range(mid_index, len(my_array)):
            right_array.append(my_array[i])

    left_sorted_array = split_and_merge(left_array)
    right_sorted_array = split_and_merge(right_array)
    return merge_sort(left_sorted_array,right_sorted_array)

print split_and_merge([2,4,6,9,7,8,4,1,10,5])