## Русский

**JSON Localization Table Generator** позволяет сгенерировать таблицу MediaWiki для русской локализации ванильного Minecraft. По умолчанию использует файл для русской локализации в активах, расположенных в стандартной директории для Windows `%appdata%/.minecraft`, а файл для оригинальной локализации `en_us.json` должен располагаться в той-же директории, что и файл `BuildTable.py`.

После запуска создаётся сортируемая таблица следующего вида:
| Ключ перевода | Англоязычное название | Русскоязычное название |
| ------------- | --------------------- | ---------------------- |
| ... | ... | ... |

Формат вывода предполагает создание ссылок для значений всех ключей перевода, не являющихся описанием.

Редактируя объекты `favorites_keys` и `unwanted_keys` в файле `BuildTable.py` можно легко настраивать то, какие именно ключи перевода будут в сгенерированной таблице. При желании можно достаточно просто адаптировать генератор под другие языки.

## English

**JSON Localization Table Generator** allows you to generate a MediaWiki table for the Russian localization of vanilla Minecraft. By default, it uses a file for Russian localization in assets located in the standard Windows directory `%appdata%/.minecraft`, a file for the original localization `en_us.json` must be located in the same directory as the file `BuildTable.py`.

After the launch, a sortable table is created with the following format:
| Translation key | English-language name | Russian-language name |
| --------------- | --------------------- | --------------------- |
| ... | ... | ... |

The output format assumes the creation of links for the values of all translation keys that are not a description.

Editing objects `favorites_keys` & `unwanted_keys` in the file `BuildTable.py` you can easily configure which translation keys will be in the generated table. If desired, you can simply adapt the generator to other languages.
