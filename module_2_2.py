first = int (input('Введите первое число: '))
second = int (input('Введите второе число: '))
third = int (input('Введите третье число: '))

if first != second and first != third and second != third:
    print('Количество равных чисел:', 0)
elif first == second == third:
    print('Количество равных чисел:', 3)
elif first == second or first == third or second == third:
    print('Количество равных чисел:', 2)

