def sort(array):
    return merge_sort(array)


def merge_sort(array):
    if len(array)<=1:
        return array
    left_arr = merge_sort(array[:len(array)//2])
    right_arr = merge_sort(array[len(array)//2:])
    return merge(left_arr, right_arr)


def merge(left, right):
    i, j = 0, 0
    temp = list()
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            i+=1
        else:
            temp.append(right[j])
            j+=1
    if i==len(left): temp.extend(right[j:])
    else: temp.extend(left[i:])
    return temp
