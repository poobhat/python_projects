import math
from random import randint

def binary_search(ls, n):
    low = 0
    high = len(ls)-1
    guess = n
    mid = None
    while low <= high:
        mid = math.ceil((low + high) / 2)
        if guess == ls[mid]:
            return mid
        elif guess < ls[mid]:
            high = mid - 1
        else:
            low = mid + 1
        print(mid)
    return mid

if __name__ == '__main__':
    Start = 9
    Stop = 99999
    limit = 100
    ls = [randint(Start, Stop) for iter in range(limit)]
    ls.sort()
    print(ls)
    n = ls[1]
    print(n)
    # ls = ['iab', 'hcb', 'gdc', 'fed', 'dfe', 'cgf', 'bhg', 'aih']
    # ls.sort()
    # print(ls)
    # n = 'iab'
    print("Position of {} in the list is {}".format(n, binary_search(ls, n)))
