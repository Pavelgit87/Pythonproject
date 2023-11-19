# Задание 2. (повышенной сложности)
#
# Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы,
# в котором вывод разбивается на слова с удалением всех знаков пунктуации (их можно взять
# из списка string.punctuation модуля string). В этом режиме должно проверяться наличие слова в выводе.


import subprocess
import string
import re

if __name__ == '__main__':

    def func(com: str, text: str):
        result = subprocess.run(com, shell=True,
                                stdout=subprocess.PIPE, encoding='utf 8')
        out = result.stdout
        for p in string.punctuation:
            if p in out:
                out_rep = out.replace(p, ' ')

        if result.returncode == 0:
            if re.search(text, out_rep):
                print(True)
            else:
                print(False)
        else:
            print("false")


    func('cat /etc/os-release', '22.04.1')




