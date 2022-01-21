print('A')
prices = [9.16, 15.64, 24.48, 52.10, 12, 98.57, 4.97, 84.29, 68.01, 45.09, 35.07, 67.36, 40.50,
          8.59, 10, 71.09, 16.12, 94, 28.84, 5.09]

for i in prices:
    rub, kop = int(i), f"{i % 1:.02f}"[2:]
    print(f"{rub} руб {kop} коп,", end=" ")

print(f"\nB")

print(f"ID first: {id(prices)} - {prices}")
prices.sort()
print(f"ID sort: {id(prices)} - {prices}")

print('C')

prices_low = sorted(prices, reverse=True)
print(prices_low)

print('D')

print(prices_low[:5])
