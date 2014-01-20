
def merge_arrays(left_array, right_array):
    i = 0
    j = 0
    k = 0
    my_array = []
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:   # lista[index] = elementul (de pe index)
            my_array.append(left_array[i])
            i +=1
        if left_array[i] > right_array[j]:
            my_array.append(right_array[j])
            j +=1
    return my_array


def split_array(my_array):
    middle_array = len(my_array)//2 # the index of the mid elem
    left_array = []
    right_array = []

    if len(my_array) < 2: # eu am facut initial cu while len(my_array) >1
        return
    else:
        for i in range(0,middle_array):
                left_array.append(my_array[i]) # creeaza stanga
        for i in range(middle_array+1, len(my_array)-1):
                right_array.append(my_array[i]) # creeaza dreapta

    split_array(left_array)
    split_array(right_array)
    return merge_arrays(left_array,right_array, my_array)


left_array = [2,5,7,9]
right_array = [4,3,1,8]

print merge_arrays(left_array, right_array)