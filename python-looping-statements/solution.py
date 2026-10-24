def countdown_with_skip(start: int) -> list:
    result = []
    n = start
    while n >= 1:
        if n == 3:
            n -= 1
            continue
        result.append(n)
        n -= 1
    return result
    """
    Using a while loop, count down from `start` to 1 (inclusive),
    appending each number to a list, but skip appending any
    number that is exactly 3 (use continue for this).
    Do not use break here.
    Return the resulting list.
    """
    pass


def find_first_negative(numbers: list) -> int | None:
    i = 0
    found = None
    while i < len(numbers):
        if numbers[i] < 0:
            found = numbers[i]
            break
        i += 1
    else:
        return None
    return found
    """
    Using a while loop with an index variable, find and return
    the first negative number in `numbers`. Use break once found.
    If no negative number exists, use the loop's else clause to
    return None after the loop completes normally.
    """
    pass


def sum_with_index(numbers: list) -> dict:
    result = {}
    total = 0
    for i, num in enumerate(numbers):
        total += num
        result[i] = total
    return result
    """
    Using a for loop with enumerate(), build and return a
    dictionary mapping each index to the running sum of all
    numbers up to and including that index.

    Example: sum_with_index([10, 20, 30])
    -> {0: 10, 1: 30, 2: 60}
    """
    pass


def manual_iteration_trace(items: list) -> list:
    result = []
    iterator = iter(items)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        result.append(item)
    return result
    """
    Without using a for loop, replicate what a for loop does
    internally: use iter() to get an iterator from `items`, then
    repeatedly call next() on it inside a while loop, catching
    StopIteration to know when to stop.

    Return a list of all elements retrieved this way, in order
    (it should exactly match the original `items` list).
    """
    pass
