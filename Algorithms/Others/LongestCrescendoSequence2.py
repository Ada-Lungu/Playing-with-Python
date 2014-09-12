__author__ = 'ada'


"""def longest_crescendo_seq1(index = 0, num_list):

    sequence_list = []
    seq_counter = 0

    current_num = num_list[index]
    next_num = num_list[index + 1]

    counter_to_sequence_list = {}

    if len(sequence_list) < (len(num_list) - len(sequence_list)):
        if current_num < next_num and seq_counter < num_list:
            seq_counter += 1
            sequence_list.append(next_num)
            longest_crescendo_seq(index+1, num_list)
        counter_to_sequence_list[seq_counter] = sequence_list"""


 # [2,4,5,7,1,3,5,6,8,9,10,4,2,1]

def longest_crescendo_seq(num_list):

    longest_crescendo_seq = []
    sequence_list = []

    for index in range(len(num_list)-1): # 13
        rest_of_num_list = (len(num_list) - len(sequence_list))
        if len(longest_crescendo_seq) > rest_of_num_list:
            return longest_crescendo_seq

        if num_list[index] < num_list[index+1]: #0 < 1
            sequence_list.append(num_list[index])   #seq_list [2,4,5,7,]
        elif len(longest_crescendo_seq) < len(sequence_list):
            sequence_list.append(num_list[index])
            longest_crescendo_seq = sequence_list[:] #long =
            sequence_list = []

    return longest_crescendo_seq


print longest_crescendo_seq([2,4,5,7,1,3,5,6,8,9,10,4,2,1])

















