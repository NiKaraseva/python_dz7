#  Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.


from random import randint


__all__ = ['write_file']


def give_names() -> str:
    name = ''
    for _ in range(randint(4, 8)):
        name += chr(randint(98, 122))
    return name.capitalize()


def write_file(name_file: str, count_line: int) -> None:
    with open(name_file + '.txt', 'w', encoding='UTF-8') as f:
        for _ in range(count_line):
            f.write(f"{give_names()}\n")


if __name__ == '__main__':
    write_file('file_names', 5)