# Переменная файла со списком значений с указанием аргументов
f = open("in.txt", encoding="utf8")
# Указание строки, с которой начинается чтение
n = 0
# Начальная позиция
i = 2
# Построковое чтение с записю содержания спрайта
for l in f:
    #   print (l)
    id = l.replace("\r", "").replace("\n", "")
    n += 1
    if (n % 2) == 1:
        en = id
    else:
        ru = id
        #       print (ru + en)
        out = (
            "      ['"
            + str(ru)
            + "'] = {['поз'] = "
            + str(i)
            + ", ['раздел'] = 1, ['en'] = '"
            + str(en)
            + "'},"
        )
        i += 1
        with open("out.txt", "a", encoding="utf8") as stream:
            stream.write(str(out) + "\n")
            stream.close()
