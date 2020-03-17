#! /usr/bin/env python3


def binary_search(array, n, integer, i):
    # this is kind of cheating in python, because we have
    # `list.index(x)` and `x in list`

    if array[n // 2] == integer:
        return i + n // 2
    if n // 2 == 0:
        return -1
    elif array[n // 2] < integer:
        return binary_search(array[n // 2 + 1:],
                             n // 2,
                             integer,
                             i + n // 2 + 1)
    else:
        return binary_search(array[:n // 2], n // 2, integer, i)


with open('binary.txt', 'r') as f:
    data = f.readlines()
    n = int(data[0].strip())
    m = int(data[1].strip())
    sorted_array = data[2].split()
    assert len(sorted_array) == n
    search_integers = data[3].split()
    assert len(search_integers) == m

sorted_array = [int(x) for x in sorted_array]
search_integers = [int(x) for x in search_integers]

results = []

for integer in search_integers:
    index = binary_search(sorted_array, n, integer, 1)
    results.append(index)

print(' '.join([str(x) for x in results]))
