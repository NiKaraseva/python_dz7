# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.


__all__ = ['read_and_write']


def read_and_write(name_file_1: str, name_file_2: str, output_file: str) -> None:
    with(open(name_file_1, 'r', encoding='UTF-8') as f1,
         open(name_file_2, 'r', encoding='UTF-8') as f2):
        names = f1.read().split('\n')
        numbers = f2.read().split('\n')

    # longest_file = max(names, numbers, key=len) #key – критерий поиска максимального значения

    if len(names) < len(numbers):
        names += names[:len(numbers) - len(names)]
    else:
        numbers += numbers[:len(names) - len(numbers)]

    with open(output_file, 'w', encoding='UTF-8') as f:
        for name, number in zip(names, numbers):
            if not name or not number:
                break
            number_output_int, number_output_float = map(float, number.split(' | '))
            mult = number_output_int * number_output_float
            if mult < 0:
                f.write(f'{name.lower()} {abs(mult)}\n')
            else:
                f.write(f'{name.upper()} {int(mult)}\n')


if __name__ == '__main__':
    read_and_write('file_names.txt', 'file_numbers.txt', 'num_with_names.txt')
