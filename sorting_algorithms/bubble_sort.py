def sort(array):
    n = len(array)
    if n < 2:
        return
    for k in range(n-1):
        flag = False
        for i in range(n-k-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                flag=True
        if not flag:
            return

