import timeit
import random


def main():

    # Створюємо списки з різною довжиною
    short_list = []
    midle_list = []
    long_list = []

    for i in range(10):
        short_list.append(random.randint(0, 100000))

    for i in range(1_000):
        midle_list.append(random.randint(0, 100000))

    for i in range(10_000):
        long_list.append(random.randint(0, 100000))

    # Визначаємо Merge sort

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        return merge(merge_sort(left_half), merge_sort(right_half))

    def merge(left, right):
        merged = []
        left_index = 0
        right_index = 0

        # Спочатку об'єднайте менші елементи
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        # Якщо в лівій або правій половині залишилися елементи,
            # додайте їх до результату
        while left_index < len(left):
            merged.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1

        return merged

    # Визначаємо Insertion sort

    def insertion_sort(lst):
        for i in range(1, len(lst)):
            key = lst[i]
            j = i-1
            while j >= 0 and key < lst[j]:
                lst[j+1] = lst[j]
                j -= 1
            lst[j+1] = key
        return lst

    # Функція для виводу результатів
    def print_result(list_type: str, list_times: list[tuple[str, float]]) -> None:
        def get_time(element):
            return element[1]
        list_times.sort(key=get_time, reverse=True)

        print(f"{list_type}:")
        for x in list_times:
            print(
                f"Сортування {x[0]:<10} займає: {x[1]:<25} секунд")

        dif_1 = round(list_times[0][1] / list_times[2][1] * 100, 2)
        dif_2 = round(list_times[1][1] / list_times[2][1] * 100, 2)
        print(
            f"Алгоритм {list_times[2][0]} швидший на {dif_1}% за алгоритм {list_times[0][0]} та швидший на {dif_2}% за алгоритм {list_times[1][0]}", end="\n\n")

    # Step 1
    # Тестуємо short list

    # визначення часу для короткого списку
    time_number_executions = 10_000
    time_merge_sort_short_list = timeit.timeit(lambda: merge_sort(
        short_list), number=time_number_executions)
    time_insection_sort_short_list = timeit.timeit(lambda: insertion_sort(
        short_list), number=time_number_executions)
    time_py_sort_short_list = timeit.timeit(
        lambda: short_list.sort(), number=time_number_executions)

    short_times = [("Merge", time_merge_sort_short_list),
                   ("Insertion", time_insection_sort_short_list),
                   ("Timsort", time_py_sort_short_list)]

    print_result("Короткий список", short_times)

    # Step 2
    # Тестуємо midle list

    time_number_executions = 1_000
    time_merge_sort_midle_list = timeit.timeit(lambda: merge_sort(
        midle_list), number=time_number_executions)
    time_insection_sort_midle_list = timeit.timeit(lambda: insertion_sort(
        midle_list), number=time_number_executions)
    time_py_sort_midle_list = timeit.timeit(
        lambda: midle_list.sort(), number=time_number_executions)

    midle_times = [("Merge", time_merge_sort_midle_list),
                   ("Insertion", time_insection_sort_midle_list),
                   ("Timsort", time_py_sort_midle_list)]

    print_result("Середній список", midle_times)

    # Step 3
    # Тестуємо long list

    time_number_executions = 1_000
    time_merge_sort_long_list = timeit.timeit(lambda: merge_sort(
        long_list), number=time_number_executions)
    time_insection_sort_long_list = timeit.timeit(lambda: insertion_sort(
        long_list), number=time_number_executions)
    time_py_sort_long_list = timeit.timeit(
        lambda: long_list.sort(), number=time_number_executions)

    long_times = [("Merge", time_merge_sort_long_list),
                  ("Insertion", time_insection_sort_long_list),
                  ("Timsort", time_py_sort_long_list)]

    print_result("Довгий список", long_times)


if __name__ == "__main__":
    main()
