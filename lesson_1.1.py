duration = int(input('Введите число: '))

second = duration % 60
minutes = duration // 60 % 60
hours = duration // 3600 % 24
day = duration // 86400

print(day, 'дн', hours, 'часов', minutes, 'минут', second, 'сек', sep=' ')
