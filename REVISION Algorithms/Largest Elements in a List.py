__author__ = 'ada'


def largest(n,xs):
  sorted_list = sorted(xs)
  highest_nums = sorted_list[-n:]
  return highest_nums

print largest(3,[2,4,6,7,9,4,0,1])


# sorted(xs, reverse= TRue)[:n]
# list[start: stop: step] => [-3:]


# sorting the list with a sorting algorithm: quick sort
def largest_from_the_scractch(n,xs):
  """Find the n highest elements in a list"""
  highest_nums = []
  sorted_xs = sort_xs(xs,0,len(xs))
  counter = 0
  while counter <= n:
    highest_nums.append(sorted_xs[len(xs)-1])
    counter +=1

  return highest_nums



def sort_xs(xs, left_margin, right_margin):
    pivot_position = left_margin + (right_margin - left_margin)//2
    pivot = xs[pivot_position]

    if right_margin > left_margin:
        for elem_pos in range(left_margin, pivot_position):
            if xs[elem_pos] > pivot:
                xs.insert(pivot_position+1, xs[elem_pos])
                del(xs[elem_pos])
                pivot_position -= 1

        for elem_pos in range(pivot_position+1,right_margin+1):
            if xs[elem_pos] < pivot:
                xs.insert(pivot_position, xs[elem_pos])
                del(xs[elem_pos])
                pivot_position += 1

    quick_sort(xs, left_margin, pivot_position-1)
    quick_sort(xs, pivot_position+1, right_margin)

    return xs

print largest_from_the_scractch(3,[2,4,6,7,9,4,0,1])