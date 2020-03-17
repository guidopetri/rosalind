#! /usr/bin/env python3


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


with open('rosalind_fibo.txt', 'r') as f:
    n = f.read().strip()

print(fibo(int(n)))
