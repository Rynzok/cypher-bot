def fast_sort(array_of_numbers):
    for i in range(len(array_of_numbers)):
        cursor = array_of_numbers[i]
        pos = i

        while pos > 0 and array_of_numbers[pos - 1] > cursor:
            # Меняем местами число, продвигая по списку
            array_of_numbers[pos] = array_of_numbers[pos - 1]
            pos = pos - 1
        # Остановимся и сделаем последний обмен
        array_of_numbers[pos] = cursor
    return array_of_numbers
