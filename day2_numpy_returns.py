import numpy as np

prices = np.array([150.0, 152.3, 151.8, 154.0, 153.5,
                   156.2, 155.0, 157.8, 159.1, 158.4])

# ЗАДАНИЕ 1: посчитай дневные доходности через срезы numpy
# подсказка: prices[1:] это все цены кроме первой
#            prices[:-1] это все цены кроме последней
daily_returns = ((prices[1:] - prices[:-1]) / prices[:-1])  # замени на формулу

# ЗАДАНИЕ 2: используй numpy-функции (не писать вручную!)
mean_return = np.mean(daily_returns)    # np.mean(...)
max_return = np.max(daily_returns)     # np.max(...)
min_return = np.min(daily_returns)    # np.min(...)
std_return = np.std(daily_returns)     # np.std(...) — стандартное отклонение, мера риска

# ЗАДАНИЕ 3: найди индекс дня с максимальной доходностью
best_day = np.argmax(daily_returns)       # np.argmax(...)

# ЗАДАНИЕ 4: отфильтруй только положительные доходности
positive_returns = daily_returns[daily_returns>0]  # подсказка: daily_returns[daily_returns > 0]

# Вывод
print("Дневные доходности:", daily_returns)
print("Средняя доходность:", mean_return)
print("Макс:", max_return, "Мин:", min_return)
print("Стандартное отклонение (риск):", std_return)
print("Лучший день (номер):", best_day)
print("Только положительные дни:", positive_returns)