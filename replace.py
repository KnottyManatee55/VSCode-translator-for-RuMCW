# Открываем файл для чтения
with open("document.txt", "r", encoding="utf8") as file:
    # Читаем содержимое файла в строку
    text = file.read()

# Чтение массива шаблонов для замены
from replacelist import patterns

# Для каждого шаблона в списке
for pattern in patterns:
    # Получаем слово для поиска и слово для замены
    search, replace = pattern
    # Заменяем все вхождения слова для поиска на слово для замены в тексте
    text = text.replace(search, replace)

# Открываем файл для записи
with open("document.txt", "w", encoding="utf8") as file:
    # Записываем измененный текст в файл
    file.write(text)