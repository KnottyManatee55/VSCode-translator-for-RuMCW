import json, re, os

# Разрешающий список
favorites_keys = {
    "^biome.",
    "^block.",
    "^color.",
    "^effect.",
    "^gamerule.",
    "advancements.",
    "container.",
    "enchantment.minecraft.",
    "entity.minecraft.",
    "filled_map.",
    "flat_world_preset." "gameMode.",
    "generator.",
    "item.minecraft.",
    "jukebox_song.",
    "painting.minecraft.",
    "trim_pattern",
    "^dataPack.",
}
# Запрещающий список
unwanted_keys = {
    "^advancements.empty",
    "^advancements.progress$",
    "^advancements.sad_label$",
    "^advancements.toast.",
    "^block.minecraft.beacon.",
    "^block.minecraft.bed/.",
    "^block.minecraft.player_head.named$",
    "^block.minecraft.spawn.not_valid$",
    "^block.minecraft.spawner.desc1$",
    "^block.minecraft.spawner.desc2$",
    "^container.beehive.bees$",
    "^container.beehive.honey$",
    "^container.enchant.$",
    "^container.enchant.clue$",
    "^container.enchant.lapis.",
    "^container.enchant.level.many$",
    "^container.enchant.level.one$",
    "^container.enchant.level.requirement$",
    "^container.isLocked$",
    "^container.repair.cost$",
    "^container.shulkerBox.itemCount$",
    "^container.shulkerBox.more$",
    "^container.shulkerBox.unknownContents$",
    "^container.spectatorCantOpen$",
    "^container.upgrade.error_tooltip$",
    "^container.upgrade.missing_template_tooltip$",
    "^effect.duration.infinite$",
    "^effect.none$",
    "^entity.minecraft.falling_block_type$",
    "^filled_map.id$",
    "^filled_map.level$",
    "^filled_map.locked$",
    "^filled_map.scale$",
    "^item.minecraft.bundle.empty$",
    "^item.minecraft.bundle.fullness$",
    "^item.minecraft.crossbow.projectile$",
    "^item.minecraft.debug_stick.empty$",
    "^item.minecraft.debug_stick.select$",
    "^item.minecraft.debug_stick.update$",
    "^item.minecraft.firework_rocket.flight$",
    "^item.minecraft.smithing_template.applies_to$",
    "^item.minecraft.smithing_template.upgrade$",
    "^dataPack.title$",
    "^dataPack.validation.",
}

# Перезапись файла LocalizationTable.mediawiki
with open("LocalizationTable.mediawiki", "w", encoding="utf8") as localization_table:
    # Запись шапки таблицы в файл
    localization_table.write(
        '{|class="wikitable sortable"\n!Ключ перевода \n!Англоязычное название\n!Русскоязычное название\n|-'
    )
    # Открытие англоязычной локализации в режиме чтения
    with open("en_us.json", "r", encoding="utf8") as en_us:
        # Преобразование строк JSON в объект Python
        en_data = json.load(en_us)
        # Открытие русскоязычной локализации в режиме чтения
    with open(
        os.getenv("appdata")
        + "\\.minecraft\\assets\\objects\\e2\\e241beb6e9c340ea2dff1d90a9f6a9487fa55add",
        "r",
        encoding="utf8",
    ) as ru_ru:
        # Преобразование строк JSON в объект Python
        ru_data = json.load(ru_ru)
    # Перебор строк объекта англоязычных ИД
    for i in en_data:
        # Сброс срабатывания фильтра плохих ключей
        ex_key = 0
        # Перебор плохих ключей
        for u in unwanted_keys:
            # Проверка ключа на не соответствие
            if bool(re.search(u, i)):
                # Вызов срабатывания фильтра плохих ключей
                ex_key = 1
        # Перечисление избранных ключей
        for f in favorites_keys:
            # Проверка срабатывания фильтра ключей и проверка на избранность
            if ex_key == 0 and bool(re.search(f, i)):
                # Проверка на то, является ли строка описанием
                if bool(re.search(".description", i)):
                    # Запись в файл отформатированных строк таблицы
                    localization_table.write(
                        "\n|"
                        + i
                        + "\n|"
                        + en_data[i]
                        + "\n|"
                        + ru_data.setdefault(i, "{{Нет}}")
                        + "\n|-"
                    )
                else:
                    # Обработка пустых строк
                    if ru_data.setdefault(i, "{{Нет}}") == "{{Нет}}":
                        # Запись в файл отформатированных строк таблицы
                        localization_table.write(
                            "\n|"
                            + i
                            + "\n|[[:en:"
                            + en_data[i]
                            + "|"
                            + en_data[i]
                            + "]]\n|{{Нет}}\n|-"
                        )
                    else:
                        # Запись в файл отформатированных строк таблицы
                        localization_table.write(
                            "\n|"
                            + i
                            + "\n|[[:en:"
                            + en_data[i]
                            + "|"
                            + en_data[i]
                            + "]]\n|[["
                            + ru_data[i]
                            + "]]\n|-"
                        )
    localization_table.write("\n|}")
    localization_table.close
