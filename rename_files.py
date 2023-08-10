# Напишите функцию группового переименования файлов.
# Она должна:
# - принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.

# Пример:
# rename(wanted_name = "video",
# count_nums=3,
# extension_old=".txt",
# extension_new=".csv",
# diapazon=[3, 6])
# foto_2002.txt -> o_20video001.csv


from pathlib import Path


__all__ = ['funk_rename']


def _get_old_name(old_name: str, digit_range: list[int]):
    if len(old_name) < digit_range[0]:
        result = ''
    elif len(old_name) <= digit_range[1]:
        result = old_name[digit_range[0] - 1:]
    else:
        result = old_name[digit_range[0] - 1:digit_range[1]]
    return result


def funk_rename(new_name: str,
                count_num: int = 3,
                old_ext: str = '.txt',
                new_ext: str = '.csv',
                digit_range: list[int] = [3, 6]):
    num = 1
    p = Path(Path().cwd())
    for file in p.iterdir():
        name_file = str(file).split('\\')[-1]
        ext = name_file.split('.')[1]
        if ext == old_ext:
            num += 1
            Path(name_file).rename(f'{_get_old_name(name_file.split(".")[0], digit_range)}'
                                   f'{new_name}'
                                   f'{(("0" * (count_num - len(str(num))) + str(num)))}.'
                                   f'{new_ext}')


if __name__ == '__main__':
    # print(_get_old_name('foto_barsa_2022', [3, 6]))
    funk_rename('video_lanka')





