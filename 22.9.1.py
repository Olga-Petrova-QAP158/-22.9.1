array = list(map(int, input("Введите целые числа в любом порядке, через пробел: ").split()))
element = float(input("Введите любое положительное целое число из полученного списка: "))

for i in range(len(array)): # проходим по всему массиву
    idx_min = i # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min: # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]
print(array)
def binary_search(array, element, left, right):
    if left > right:
            return right
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

print(array)
left = int(array[0])
right = int(array[-1])
if element < left or element > right:
    print('Числа нет в диапазоне')
else:
    print(binary_search(array, element, 0, len(array) - 1))