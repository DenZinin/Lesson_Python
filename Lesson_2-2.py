spisok = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, val in enumerate(spisok):
    if val.isdigit():
        spisok[i] = f'"{int(val):02}"'
    elif val[1:].isdigit():
        spisok[i] = f'"{val[0]}{int(val[1:]):02}"'

print(" ".join(spisok))
