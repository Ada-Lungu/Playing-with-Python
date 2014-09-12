__author__ = 'ada'

def bubble_sort(unsorted_list):

    list_lenght = len(unsorted_list)
    while list_lenght > 1:
        for position in range(0, list_lenght-1):
            elem = unsorted_list[position]
            next_elem = unsorted_list[position+1]
            if elem > next_elem:
                replacer = elem
                elem = next_elem
                next_elem = replacer
            elif elem == next_elem:
                unsorted_list.remove(unsorted_list[position])
        list_lenght -= 1

    sorted_list = unsorted_list
    return sorted_list


# the bubble_sort optimized reversely: rabbits from turtles
def bubble_sort_version2_switches(sort_list):

    switches = True
    list_length = len(sort_list)

    while list_length > 1 and switches == True:
        switches = False
        for position in range(0, list_length-1):
            elem = sort_list[position]
            next_elem = sort_list[position+1]
            if elem > next_elem:
                sort_list[position], sort_list[position+1] = sort_list[position+1], sort_list[position]
                switches = True
        list_length -= 1
    return sort_list


print bubble_sort_version2_switches([3,3,5,7,8,10,4,15,12,9])


# Optimization Rabbits
def bubble_sort(list):

    right_limit = len(list)
    left_limit = 0
    switches = True

    while switches == True:
        switches = False   
        for position in range(left_limit, right_limit-1):
            if list[position] > list[position + 1]:
                list[position], list[position+1] = list[position+1], list[position]
                switches = True
        right_limit -= 1

        # switches = False
        for position in range(right_limit-1, left_limit-1, -1):
            if list[position+1] < list[position]:
                list[position], list[position+1] = list[position+1], list[position]
                switches = True
        left_limit += 1

    return list

print bubble_sort([5,6,7,9,2,1,4,12,10])



# INSERSION Sort ALGORITHM

def insertion_sort(unsorted_list):

    for position in range(1, len(unsorted_list)):
        for second_position in range(position-1, 0):
            if unsorted_list[position] > unsorted_list[second_position]:
                unsorted_list.insert(second_position+1, unsorted_list[position])


def bubble_sort_reversed_optim(list):
    right_margin = len(list)
    left_margin = 0
    sorted = False

    while not sorted:
        sorted = True
        for position in range(left_margin, right_margin-1):
            if list[position] > list[position+1]:
                list[position], list[position+1] = list[position+1], list[position]
                sorted = False
        right_margin -= 1

        for position in range(right_margin,left_margin, -1):
            if list[position] < list[position-1]:
                list[position], list[position-1] = list[position-1], list[position]
                sorted = False
        left_margin += 1

    return list

print bubble_sort_reversed_optim([5,6,7,9,2,1,4,12,10])


def bubble_sort_optimized_reversed(list):
#     right margin/ left margin
    right_margin = len(list)
    left_margin = 0
    sorted = False

    while not sorted: # sorted = False
        sorted = True
        for elem_position in range(left_margin,right_margin-1):
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

print bubble_sort_optimized_reversed([2, 4, 7, 6, 0, 10, 19])
























