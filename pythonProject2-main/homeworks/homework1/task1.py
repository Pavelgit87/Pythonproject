
# Задание 1.
#
# Условие:
# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе
# и False в противном случае.
# Передаваться должна только одна строка, разбиение вывода использовать не нужно.


import subprocess
import re


if __name__ == '__main__':

    def func(com: str, text: str):
        result = subprocess.run(com, shell=True,
                                stdout=subprocess.PIPE, encoding='utf 8')
        out = result.stdout
        # print(out)
        if result.returncode == 0:
            if re.search(text, out):
                print(True)
            else:
                print(False)
        else:
            print(False)


    func('cat /etc/os-release', 'jammy')

