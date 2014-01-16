
def merge_sort(my_array):
    # we split the array in 2 halves and compare the elements
middle_array = len(my_array)//2 # the index of the mid elem
left_array = []
right_array = []

n = len(my_array)

    while len(my_array) > 1:
        middle_array = len(my_array)//2
        for each_elem in my_array:
            if each_elem in range(0,len(middle_array):
                left_array.append(each_elem)
            if each_elem in range(len(middle_array), len(my_array)):
                right_array.append(each_elem)

    i = 0
    j = 0
    k = 0

    # ---- here they must go sorted

    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:# lista[index] = elementul (de pe index)
            new_array.append(k, left_array[i])
            i +=1
            k +=1
        if left_array[i] > right_array[j]:
            new_array.append(k, right_array[j])
            j +=1
            k +=1


