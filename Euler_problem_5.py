# Euler problem 5:

a = 0
b = 0
while a != 20:             # Встановлюємо лічильник (якщо а == 20 то цикл припиняється)
    a = 0                  # Обнуляємо лічильник після кожної "невдалої" ітерації циклу for
    b += 20                # Ставимо крок 20 (мінімальне число, що ділиться на 20)
    for i in range(1,21):  # Запускаємо цикл, щоб перевірити чи це число ділиться на кожне з 20 без залишку
        if b % i == 0:     # Якщо так -
            a += 1         # Додаємо до а одиницю, якщо ні - то з нового циклу while лічильник обнуляється

print(b)









