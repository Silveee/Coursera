# python3

def sort(data, index, swaps):
    root = data[index]
    left = 2*index + 1
    right = left + 1
    if left > len(data) - 1:
        return
    if right > len(data) - 1:
        if data[left] < root:
            data[index], data[left] = data[left], data[index]
            swaps.append((index, left))
        return

    if root < data[left] and root < data[right]:
        return
    swap = left if data[left] < data[right] else right
    data[swap], data[index] = data[index], data[swap]
    swaps.append((index, swap))
    return sort(data, swap, swaps)

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []
    for i in range(len(data)):
        sort(data, len(data) - i - 1, swaps)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
