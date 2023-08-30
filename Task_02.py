S = int(input("Введите значение S: "))
P = int(input("Введите значение P: "))
X = (S-int((S**2-4*P)**0.5))//2
Y = S - X
print(f'Задуманные числа: {X, Y}') if X<=1000 and Y<=1000 else print ("Неверные числа")