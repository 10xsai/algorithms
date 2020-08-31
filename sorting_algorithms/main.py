from datetime import datetime as dt
from insertion_sort import sort as isort
from selection_sort import sort as ssort
from bubble_sort import sort as bsort
from merge_sort import sort as msort
import random
import bubble_sort, insertion_sort, selection_sort

n = 20000
array = list()
while n > 0:
    array.append(random.randint(1, 100000))
    n-=1

print("started operation")
t0 = dt.now()

ssort(array.copy())
t1 = dt.now()


bsort(array.copy())
t2 = dt.now()


isort(array.copy())
t3 = dt.now()

msort(array.copy())
t4 = dt.now()

print(f'selection sort: {t1-t0}s')
print(f'bubble sort: {t2-t1}s')
print(f'insertion sort: {t3-t2}s')
print(f'merge sort: {t4-t3}s')
