def almost_all(numbers):
    sumall = sum(numbers)
    for i in range(len(numbers)):
        numbers[i] = sumall - numbers[i]

    return numbers

print(almost_all([1,2,3]))

import random

numbers = list(range(123456, 123456 + 10 ** 5))
random.shuffle(numbers)
print(almost_all(numbers))