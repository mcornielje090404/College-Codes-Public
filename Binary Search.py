def binary_search(cards, number):
    start, end = 0, len(cards)-1

    while start <= end:
        mid = (start + end) / 2
        current = cards[mid]

        if cards[mid] == number:
            if mid-1 >= 0 and cards[mid-1] == number:
                end = mid - 1
            else:
                return mid
        elif card[mid] < number:
            end = mid - 1
        else:
            start = mid + 1

    return -1

cards = [212, 198, 156, 138, 122, 95, 83, 64, 42, 20, 7, 1]
number = 95
result = binary_search(cards, number)
print(result)
