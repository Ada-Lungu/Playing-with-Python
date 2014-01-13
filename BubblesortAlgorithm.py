
# Variant 3 is working:), skip the rest if not interested in the evolution of my thoughts:P:)
# my first try
def bubble_sort(any_list): #[2, 3, 5,  8, 1]
    count = len(any_list)
    while count > 1:
        for i in range(0, len(any_list)-1):
            if any_list[i] > any_list[i+1]:
               a, b = any_list.index(any_list[i+1]), any_list.index(any_list[i]) # indexul elementelor mele de comparat
               any_list[a], any_list[b] = any_list[b], any_list[a]
            count = count + (len(any_list)-1)
    return any_list

# my second try
def bubble_sort2(my_list):
    eradicate_list = my_list
    while len(eradicate_list) > 1:
        for i in range(0, len(my_list)-1):
            for each_elem in my_list:
                if my_list[i] > my_list[i+1]:
                    a, b = my_list.index(my_list[i+1]), my_list.index(my_list[i]) # indexul elementelor mele de comparat
                    my_list[a], my_list[b] = my_list[b], my_list[a]
        del(my_list[len(my_list)])
    return my_list

# a lil' more research and 3rd try

def bubble_sort3(my_list):  #[2, 3, 5, 1, 8]
    count = 0
    #while count < len(my_list):
    for i in range(0,len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i] > my_list[j]:
                a, b = my_list.index(my_list[i]), my_list.index(my_list[j]) # indexul elementelor mele de comparat
                my_list[a], my_list[b] = my_list[b], my_list[a]
        count +=1
    print count
    return my_list

lista_mea = [2, 3, 5, 1, 8, 11, 18, 24, 20, 19, 40, 38, 21,50,34,59,52,56,42,90,82,85,83,98]
print bubble_sort3(lista_mea)


























