from merge_sort import sort
import random

n = 100

array = list()

while n > 0:
    array.append(random.randint(1, 10000))
    n-=1

array = sort(array)
print(array)