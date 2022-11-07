
def is_even(number: float) -> bool:
    return number % 2 == 0


my_number = 10.5
is_my_number_even = is_even(my_number)

if is_my_number_even:
    print(f'{my_number} is even!')
else:
    print(f'{my_number} is not even!')
