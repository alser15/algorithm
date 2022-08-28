def binary_searches(list_: [int], items: int):
    low = 0
    high = len(list_) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = list_[mid]
        if guess == items:
            return mid
        elif guess > items:
            high = mid - 1
        else:
            low = mid + 1
    return None
