__author__ = 'ada'


def print_numbers(limit_up):

    if limit_up >= 0:
        print limit_up
        print_numbers(limit_up - 1)

print_numbers(1000)


