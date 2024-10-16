# Порівняльний аналіз алгоритмів сортування

## Опис завдання

Провести порівняльний аналіз трьох алгоритмів сортування: Merge Sort, Insertion Sort та Timsort. Мета — оцінити їх ефективність на наборах даних різної довжини та підтвердити теоретичні оцінки складності на практиці.

## Результати тестування

### Короткий список (10 елементів):

-   Merge Sort: 0.00815 секунд
-   Insertion Sort: 0.00098 секунд
-   Timsort: 0.00012 секунд

Timsort швидший на 6825.88% за Merge Sort та на 824.71% за Insertion Sort.

### Середній список (1000 елементів):

-   Merge Sort: 1.787 секунд
-   Insertion Sort: 0.149 секунд
-   Timsort: 0.0043 секунд

Timsort швидший на 41846.38% за Merge Sort та на 3501.96% за Insertion Sort.

### Довгий список (10000 елементів):

-   Merge Sort: 23.63 секунд
-   Insertion Sort: 3.13 секунд
-   Timsort: 0.048 секунд

Timsort швидший на 48946.75% за Merge Sort та на 6486.33% за Insertion Sort.

## Висновки

Алгоритм Timsort є значно ефективнішим, особливо на більших наборах даних. Це підтверджує, що його комбінація Merge Sort та Insertion Sort дозволяє досягти кращої продуктивності порівняно з класичними методами.
