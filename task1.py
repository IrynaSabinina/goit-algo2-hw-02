def find_min_max(arr):
    # Якщо масив порожній
    if not arr:
        raise ValueError("Масив не може бути порожнім.")

    # Якщо в масиві лише один елемент
    if len(arr) == 1:
        return arr[0], arr[0]

    # Якщо два елементи — порівнюємо напряму
    if len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])

    # Розділення масиву навпіл
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    # Об’єднання результатів
    overall_min = left_min if left_min < right_min else right_min
    overall_max = left_max if left_max > right_max else right_max

    return overall_min, overall_max


# 🔹 Приклад використання:
arr = [5, 2, 9, 1, 7, 3, 6]
print(find_min_max(arr))  # ➜ (1, 9)
