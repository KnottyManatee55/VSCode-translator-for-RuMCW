from slpp import slpp
from PIL import Image
import re

# Запрещённые символы в названии
bad_symbols = ["-", "/"]

# Открытие спрайта
with open("./WikiSprite.lua", "r", encoding="utf8") as file:
    # Читаем содержимое файла в строку
    wiki_sprite_raw = file.read()
# Исключение названия массива
wiki_sprite_raw = wiki_sprite_raw.replace("return", "")
# Преобразование мета-таблицы LUA в словарь Python
wiki_sprite = slpp.decode(wiki_sprite_raw)

# Название мода в переменную
mod_name = wiki_sprite["настройки"]["имя"]
# Выяснения названия изображения спрайта из настроек спрайта, если они не указаны, задаётся стандартное
image = wiki_sprite["настройки"].get("изобр", mod_name + "CSS.png").replace(" ", "_")
# Размер клетки
size = wiki_sprite["настройки"]["разм"]
# Открытие картинки
im = Image.open(image)
# Проверка, анимированно ли изображение
if im.is_animated:
    print("Внимание!!!\nИзображение анимированно")
# Вычисление количества элементов в строке спрайта
item_format = wiki_sprite["настройки"]["формат"] / wiki_sprite["настройки"]["разм"]
# Псевдонимы
aliases_list = "return {\n"


# Проверка и добавление англоязычного названия в псевдоним в случае если оно указано для названий с запрещёнными символами
def get_en_name(pattern):
    if wiki_sprite["IDы"][pattern].get("en") != None:
        en_name = ', english = "' + wiki_sprite["IDы"][pattern]["en"] + '"'
    return en_name


# Создание псевдонима для запрещённых символов
def aliases_fix_proc(pattern, pattern_fix):
    aliases_fix = (
        '	["'
        + pattern
        + '"] = { title = "'
        + pattern
        + '", name = "'
        + pattern_fix
        + '"'
        + get_en_name(pattern)
        + " },\n"
    )
    return aliases_fix


# Перечисление спрайта
for pattern in wiki_sprite["IDы"]:
    # Исключение заглушки Неизвестно из генерации
    if pattern != "Неизвестно":
        # Определение позиции спрайта
        x_sprite = (int(wiki_sprite["IDы"][pattern]["поз"]) - 1) % item_format
        y_sprite = (int(wiki_sprite["IDы"][pattern]["поз"]) - 1) // item_format
        x = x_sprite * size
        y = y_sprite * size
        box = (x, y, x + size, y + size)
        # Получение иконки со спрайта
        region = im.crop(box)
        im_out = Image.new("RGBA", (size, size), (255, 0, 0, 0))
        im_out.paste(region)
        # Проверка наличия плохих символов
        if ":" in pattern or "/" in pattern:
            if ":" in pattern:
                pattern_fix = pattern.replace(":", "-")
                img_name = "Grid " + pattern_fix + " (" + mod_name + ").png"
                # Запись псевдонима
                aliases_list = aliases_list + aliases_fix_proc(pattern, pattern_fix)
            if "/" in pattern:
                pattern_fix = pattern.replace("/", "-")
                img_name = "Grid " + pattern_fix + " (" + mod_name + ").png"
                # Запись псевдонима
                aliases_list = aliases_list + aliases_fix_proc(pattern, pattern_fix)
        else:
            img_name = "Grid " + pattern + " (" + mod_name + ").png"
            # Запись псевдонима для англоязычного названия, если оно есть
            if wiki_sprite["IDы"][pattern].get("en") != None:
                aliases_list = (
                    aliases_list
                    + '	["'
                    + pattern
                    + '"] = { name = "'
                    + pattern
                    + '"'
                    + ', english = "'
                    + wiki_sprite["IDы"][pattern]["en"]
                    + '" },\n'
                )
        im_out.save(img_name)
        im_out = Image.open(img_name)
# Закрытие списка псевдонимов
aliases_list = re.sub(",\n$", "\n}", aliases_list)
# Сохранение псевдонимов
with open("Aliases.lua", "w", encoding="utf-8") as file:
    file.write(aliases_list)
