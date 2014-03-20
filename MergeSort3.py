
def merge_list(first_half, second_half):
    i = 0
    j = 0
    merged_list = []

    # if merged_list < len(unsorted_list): - credeam ca fac merge aici pana cand am array-ul la lungimea initiala

    while i <= len(first_half) and j <= len(second_half):
        if (i == len(first_half)):
            merged_list.append(second_half[j])
            j += 1
        elif (j == len(second_half)):
            merged_list.append(first_half[i])
            i += 1
        elif (first_half[i] <= second_half[j]):
            merged_list.append(first_half[i])
            i += 1
        elif (second_half[j] <= first_half[i]):
            merged_list.append(second_half[j])

    return merged_list


def split_and_merge(unsorted_list):
    # first we just split the list in halves in subsequent lists until there are lists of only 1 element

    first_half = []
    second_half = []

    if len(unsorted_list) < 2: # an array with one element, is ... sorted!
        return unsorted_list
    else:
        # len(unsorted_list) > 1:
        for i in range(0, len(unsorted_list)//2):
            first_half.append(unsorted_list[i])
        for j in range(len(unsorted_list)//2, len(unsorted_list)):
            second_half.append(unsorted_list[j])

    first_sorted_half = split_and_merge(first_half)
    second_sorted_half = split_and_merge(second_half)

    return merge_list(first_sorted_half, second_sorted_half)



left_array = [2, 5, 7, 9]
right_array = [1, 3, 7, 8, 11, 9]

print merge_list(left_array, right_array)




