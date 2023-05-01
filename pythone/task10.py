n = int(input("Введите количество монеток: "))
coins = input("Введите состояние монеток (орел - 1, решка - 0): ")
count_heads = 0
count_tails = 0
for i in coins:
    if i == '1':
        count_tails += 1
    else:
        count_heads += 1
print(min(count_heads, count_tails))