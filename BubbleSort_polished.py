
def bubble_sort(my_list):  #[2, 3, 5, 1, 8]
    count = 0
    #while count < len(my_list):
    for i in range(0,len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i] > my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
        count +=1
    print count
    return my_list

lista_mea = [2, 3, 5, 1, 8, 11, 18, 24, 20, 19, 40, 38, 21,50,34,59,52,56,42,90,82,85,83,98, 76, 72, 79, 63, 34,44,100,109,105]
print bubble_sort(lista_mea)