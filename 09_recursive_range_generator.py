# Description: Uses clean procedural call-stacks to construct incremental list arrays recursively without loop expressions.
def range_of_numbers(start_num, end_num):
    if start_num == end_num:
        return [start_num]
    
    numbers_list = range_of_numbers(start_num, end_num - 1)
    numbers_list.append(end_num)
    return numbers_list
