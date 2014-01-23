# takes two sorted lists
# must return a new sorted list
def merge_arrays(left_array, right_array):
    i = 0
    j = 0
    my_array = []
    while i < len(left_array) or j < len(right_array):

        # we are finished with left array
        if (i == len(left_array)):
            # copy everything that remains from the right_array
            my_array.append(right_array[j])
            j+=1
        elif (j == len(right_array)):
            #copy everything that remains from left array
            my_array.append(left_array[i])
            i+=1
        elif (left_array[i] <= right_array[j]):   # lista[index] = elementul (de pe index)
            my_array.append(left_array[i])
            i += 1
        elif left_array[i] > right_array[j]:
            my_array.append(right_array[j])
            j += 1
    return my_array


# always returns an array which is sorted...
def split_and_merge_array(my_array):
    middle_array = len(my_array) // 2 # the index of the mid elem
    left_array = []
    right_array = []

    if len(my_array) < 2: # an array with one element, is ... sorted!
        return my_array # asta nu inteleg - ce returneaza
    else:
        #split
        for i in range(0, middle_array):
            left_array.append(my_array[i]) # creeaza stanga
        for i in range(middle_array, len(my_array)):
            right_array.append(my_array[i]) # creeaza dreapta

    left_sorted_array = split_and_merge_array(left_array)
    right_sorted_array = split_and_merge_array(right_array)
    #merge...
    return merge_arrays(left_sorted_array, right_sorted_array)


left_array = [2, 5, 7, 9]
right_array = [1, 3, 7, 8, 11, 9]


print merge_arrays(left_array, right_array)

"""print split_and_merge_array([10,20,4,1,4,2,8])

print split_and_merge_array([])
print split_and_merge_array([-1])"""