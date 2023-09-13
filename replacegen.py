# Переменная файла со снипетами с указанием аргументов
f = open("snippets.txt", encoding="utf8")
# Указание строки, с которой начинается чтение
n = 0
# Очистка файла replacelist.py и задание названия массива
with open("replacelist.py", "w", encoding="utf8") as stream:
    stream.write("patterns = [" + "\n")
    stream.close()
# Построковое чтение сниппетов и их запись в файл замен
for l in f:
    # print(l)
    id = l.replace("\r", "").replace("\n", "")
    n += 1
    if (n % 2) == 1:
        find = id
    else:
        replace = id
        # print(find + replace)
        out = '    ("' + str(find) + '", "' + str(replace) + '"),'
        # print(out)
        with open("replacelist.py", "a", encoding="utf8") as stream:
            stream.write(str(out) + "\n")
            stream.close()
# Закрытие массива
with open("replacelist.py", "a", encoding="utf8") as stream:
    stream.write("]")
    stream.close()
