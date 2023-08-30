import random
from random import randint

total_coins = int(input("Введите количество монеток: "))
Orel = 0
Reshka = 0
coins = [0, 1]
for i in range(total_coins):
    random.shuffle(coins)
    if int(coins[0]) == 0:
        Reshka += 1
    if int(coins[0]) == 1:
        Orel += 1
if Orel > Reshka:
    res = Reshka
else:
    res = Orel

print(f"Минимальное количество монет, которые нужно перевернуть: {res}")
