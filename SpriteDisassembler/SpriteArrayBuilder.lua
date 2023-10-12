local sprite = require('Thermal_Expansion_1')
local FileIDList = ".\\" .. sprite['настройки']['имя'] .. ".py"
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
        if v["en"] then
            FileiIDListWrite:write('    ("' .. i .. '", "' .. v['поз'] .. '", "' .. v["en"] .. '"),\n')
        else
            FileiIDListWrite:write('    ("' .. i .. '", "' .. v['поз'] .. '"),\n')
        end
    end
end
FileiIDListWrite:write("]")
FileiIDListWrite:close()
