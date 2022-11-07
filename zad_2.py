
def multiply_numbers_for(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2
    return numbers


def multiply_numbers_list(numbers):
    return [(number*2) for number in numbers]


numbers = [2, 4, 8, 16, 32]
numbers = multiply_numbers_for(numbers)
print(numbers)
numbers = multiply_numbers_list(numbers)
print(numbers)
