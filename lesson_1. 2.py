cube_list = []
cube_list_2 = []
all_sum = 0

for i in range(1, 1001):
    if i % 2 != 0:
        cube = i ** 3
        cube_list.append(cube)

for m in cube_list:
    sum_n = 0
    n = m
    while n:
        sum_n += n % 10
        n = n // 10
    if sum_n % 7 == 0:
        all_sum += m

print(all_sum)

for d in cube_list:
    cube_list_2.append(d + 17)

all_sum = 0

for m in cube_list_2:
    sum_n = 0
    n = m
    while n:
        sum_n += n % 10
        n = n // 10
    if sum_n % 7 == 0:
        all_sum += m

print(all_sum)
