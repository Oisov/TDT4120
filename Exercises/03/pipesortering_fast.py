#!/usr/bin/python3

from sys import stdin
from random import choice


def sort_list(a):
    if len(a) <= 1:
        return a
    else:
        less = []
        more = []
        pivot = choice(a)
        for i in a:
            if i < pivot:
                less.append(i)
            if i > pivot:
                more.append(i)
        less = sort_list(less)
        more = sort_list(more)
        return less + [pivot] * a.count(pivot) + more


def bisect_left(A, value, is_sorted=False):
    if value < A[0]:
        return A[0]
    elif not is_sorted:
        A = sort_list(A)

    low = 0
    high = len(A) - 1
    mid = (low + high) // 2
    last_val = A[high]
    mid_val = A[mid]
    while True:
        if value > mid_val:
            low = mid
        elif value < mid_val:
            high = mid
        else:
            return mid_val

        mid = (low + high) // 2
        if A[mid] != mid_val and A[mid] < last_val:
            mid_val = A[mid]
        else:
            return A[mid]


def bisect_right(A, value, is_sorted=False):
    if value > A[-1]:
        return A[-1]
    elif not is_sorted:
        A = sort_list(A)

    low = 0
    high = len(A) - 1
    mid = (low + high + 1) // 2
    first_val = A[low]
    mid_val = A[mid]
    while True:
        if value > mid_val:
            low = mid + 1
        elif value < mid_val:
            high = mid
        else:
            return mid_val

        mid = (low + high) // 2
        if A[mid] != mid_val and A[mid] > first_val:
            mid_val = A[mid]
        else:
            return A[mid]


def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))

    sorted_list = sort_list(input_list)

    for line in stdin:
        word = line.split()
        print(
            str(bisect_left(sorted_list, int(word[0]), True)) + " " +
            str(bisect_right(sorted_list, int(word[1]), True)))


if __name__ == "__main__":
    main()
    # A = [0, 1, 2, 3, 10, 20, 123, 1899, 2000]
    # print(bisect_left(A, 15, True))
    # print(bisect_right(A, 15, True))
    # print(sort_list([1, 0, 2, 3, 20, 10, 2000, 1899, 123]))
