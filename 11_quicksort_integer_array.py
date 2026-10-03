# Description: Uses divide-and-conquer logic arrays to build out low-overhead Quicksort array sorting rules.
def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    
    return quick_sort(less) + equal + quick_sort(greater)
