__author__ = 'ada'

def longest_crescendo_seq(num_list):

    longest_crescendo_seq = []
    crescendo_seq = []

    for index in range(len(num_list)-1):
        if len(longest_crescendo_seq) > len(num_list) - index
            return longest_crescendo_seq()

        if num_list[index] < num_list[index+1]:
            crescendo_seq.append(num_list[index])
        else:
            crescendo_seq.append(num_list[index])
            if len(longest_crescendo_seq) < len(crescendo_seq):
                longest_crescendo_seq = crescendo_seq[:]

                crescendo_seq = []

    return longest_crescendo_seq


print longest_crescendo_seq([2,4,5,7,1,3,5,6,8,9,10,4,2,1])