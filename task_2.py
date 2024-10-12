
def merge_k_lists(list_of_lists: list):
    args = list_of_lists
    merged = []
    indexes = [0] * len(args)
    total_length = 0

    for list in args:
        total_length += len(list)

    for _ in range(total_length):
        the_smaller = args[0][indexes[0]]
        the_smaller_index = 0

        # знайти наймешний
        for j in range(1, len(indexes)):
            if args[j][indexes[j]] < the_smaller:
                the_smaller = args[j][indexes[j]]
                the_smaller_index = j

        # додати найменше значення
        # посунути вказівник на крок далі
        # якщо вклазівник більший за довжину списка - видалити вказівник та список
        merged.append(the_smaller)
        indexes[the_smaller_index] += 1

        if len(args[the_smaller_index]) == indexes[the_smaller_index]:
            del indexes[the_smaller_index]
            del args[the_smaller_index]

    return merged


lists = [[1, 4, 5], [1, 3, 4], [2, 6], [3, 55, 77]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
