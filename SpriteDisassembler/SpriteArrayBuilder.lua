local sprite = require('WikiSprite')
local FileIDList = ".\\SpriteArray.py"
FileiIDListWrite = io.open(FileIDList, "w")
FileiIDListWrite:write("format=" .. sprite['настройки']['формат'] ..
    "\nsize=" .. sprite['настройки']['разм'] ..
    '\nmodname="' .. sprite['настройки']['имя'] ..
    '"\npatterns = [\n')
local format = sprite['настройки']['формат']
local size = sprite['настройки']['разм']
local idlist = sprite['IDы']
for i, v in pairs(idlist) do
    if i ~= "Неизвестно" then
        FileiIDListWrite:write('    ("' .. i .. '", "' .. v['поз'] .. '"),\n')
    end
end
FileiIDListWrite:write("]")
FileiIDListWrite:close()
