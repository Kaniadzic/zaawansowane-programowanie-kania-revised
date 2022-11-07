
def is_in_list(check_list: list, number: int) -> bool:
    return number in check_list


print(is_in_list([2, 4, 8, 16, 'X'], 4))
print(is_in_list([2, 4, 8, 16, 'X'], 144))
