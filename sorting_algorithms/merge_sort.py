def sort(array):
    merge_sort(array, 0, len(array)-1)  


def merge_sort(array, left, right):
    if left >= right:
        return

    middle = (left+right)/2

    merge_sort(array, left, middle-1)
    merge_sort(array, middle+1, right)
    merge_halves(array, left, right)



def merge_halves(array, left, right):
    