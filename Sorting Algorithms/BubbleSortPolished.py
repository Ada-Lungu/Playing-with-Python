
def bubble_sort(my_list): #[2, 3, 5, 1, 8]
    searches = 0
    swaps = 0
    not_sorted_yet = True
    while not_sorted_yet:
        not_sorted_yet = False # ==> sorted
        for i in range(0, len(my_list)-1):
            j = i + 1
            if my_list[i] > my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
                swaps +=1
                not_sorted_yet = True
        searches +=1
    print searches, swaps
    return my_list

lista_mea = [2, 3, 5, 1, 8, 11, 18, 24, 20, 19, 40, 38, 21,50,34,59,52,56,42,90,82,85,83,98, 76, 72, 79, 63, 34,44,100]
print bubble_sort(lista_mea)


