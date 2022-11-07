
def merge_lists(first_list: list, second_list: list) -> set:
    merged_list: set = []

    for i in first_list + second_list:
        if i**3 not in merged_list:
            merged_list.append(i**3)

    return merged_list


my_list = merge_lists(
    [2, 4, 8],
    [3, 4, 2]
)
print(my_list)
