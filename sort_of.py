def sort_of(numbers):
    result = []
    smallest = numbers[-1]

    for i in range(len(numbers)):
        current = numbers[-i]
        if (current <= smallest):
            result.insert(0, current)
            current = smallest

    return result

print(sort_of([3,1,7,2,5,6]))