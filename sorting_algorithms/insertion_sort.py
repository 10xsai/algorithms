def sort(array):
    n = len(array)
    if n < 2:
        return
    for i in range(1, n):
        value = array[i]
        hole = i
        while hole>0 and array[hole-1]>value:
            array[hole] = array[hole-1]
            hole -= 1
        array[hole]=value