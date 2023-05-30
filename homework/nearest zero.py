# 84164098
from typing import List, Tuple


def get_length(houses: List[int], n: int) -> List[int]:
    length = [n] * n
    zero = [i for i in range(n) if houses[i] == 0]
    left = zero[0]
    right = zero[-1]

    for i in range(left, n):
        if houses[i] != 0:
            length[i] = length[i - 1] + 1
        else:
            length[i] = 0
    for i in range(right, left, -1):
        if houses[i] != 0:
            length[i] = min(length[i], length[i + 1] + 1)
        else:
            length[i] = 0
    for i in range(left - 1, -1, -1):
        length[i] = length[i + 1] + 1
    return length


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    houses = [int(i) for i in input().split()]
    return houses, n


def main():
    houses, n = read_input()
    print(*get_length(houses, n))


if __name__ == '__main__':
    main()
