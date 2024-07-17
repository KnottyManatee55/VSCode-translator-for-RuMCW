local sprite = require('WikiSprite')
local FileAliasesList = ".\\EnglishAliases.lua"
AliasesList = io.open(FileAliasesList, "w")
AliasesList:write("return {\n")
local FileSpriteGridList = ".\\SpriteArray.py"
SpriteGridList = io.open(FileSpriteGridList, "w")
SpriteGridList:write("format=" .. sprite['настройки']['формат'] ..
    "\nsize=" .. sprite['настройки']['разм'] ..
    '\nmodname="' .. sprite['настройки']['имя'] ..
    '"\npatterns = [\n')
local format = sprite['настройки']['формат']
local size = sprite['настройки']['разм']
local idlist = sprite['IDы']
for i, v in pairs(idlist) do
    if i ~= "Неизвестно" then
        if i:find(":") then
            SpriteGridList:write('    ("' .. i:gsub(": ", " - ") .. '", "' .. v['поз'] .. '"),\n')
            if v['en'] then
                AliasesList:write('	["' ..
                    i ..
                    '"] = { title = "' ..
                    i .. '", name = "' .. i:gsub(": ", " - ") .. '", english = "' .. v['en'] .. '" },\n')
            end
        else
            SpriteGridList:write('    ("' .. i .. '", "' .. v['поз'] .. '"),\n')
            if v['en'] then
                AliasesList:write('	["' .. i .. '"] = { name = "' .. i .. '", english = "' .. v['en'] .. '" },\n')
            end
        end
    end
end
AliasesList:write("}")
AliasesList:close()
SpriteGridList:write("]")
SpriteGridList:close()
