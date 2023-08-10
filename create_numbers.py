# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.


from random import randint, uniform


__all__ = ['create_file']


MIN_VALUE = -1000
MAX_VALUE = 1000


def create_file(name_file: str, count_line: int) -> None:
    with open(name_file + '.txt', 'w', encoding='UTF-8') as f:
        for _ in range(count_line):
            f.write(f"{randint(MIN_VALUE, MAX_VALUE)} | {round(uniform(MIN_VALUE, MAX_VALUE), 2)}\n")


if __name__ == '__main__':
    create_file('file_numbers', 9)