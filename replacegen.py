import codecs
a1 = str('		"')
a2 = str('": {\n			"find": ')
a3 = str('\n			"replace": ')
a4 = ('"\n		},')
a5 = str('sprite')
n = 0
i = 3
f = open('in.txt', encoding="utf8")
for l in f:
    # print (l)
    id = (l.replace("\r", "").replace("\n", ""))
    n += 1
    if (n % 2) == 1:
        find = id
    else:
        replace = id
        # print (find + replace)
        out = a1 + str(a5) + str(i) + str(a2) + str(find) + str(a3) + str(replace) + str(a4)
        print (out)
        i += 1
        with codecs.open("out.txt", "a", "utf-8") as stream:
            stream.write(str(out) + "\n")
            stream.close()