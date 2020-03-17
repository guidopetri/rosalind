#! /usr/bin/env python3


def fibo(n):
    # early exit
    if n < 2:
        return n

    res = [0, 1]

    for i in range(2, n + 1):
        res.append(res[i - 1] + res[i - 2])

    return res[n]


with open('rosalind_fibo.txt', 'r') as f:
    n = f.read().strip()

print(fibo(int(n)))
