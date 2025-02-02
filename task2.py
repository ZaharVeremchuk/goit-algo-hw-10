import random
import matplotlib.pyplot as plt
import numpy as np

# Функція
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Кількість випадкових точок
n = 10000

# Генеруємо випадкові точки
x_rand = [random.uniform(a, b) for _ in range(n)]
y_rand = [random.uniform(0, f(b)) for _ in range(n)] 

# Рахуємо кількість точок під кривою
points_under_curve = sum(1 for x, y in zip(x_rand, y_rand) if y <= f(x))

# Рахуємо площу
area = (b - a) * f(b) * points_under_curve / n

print("Площа методом Монте-Карло:", area)

# Графік
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))

# Показуємо випадкові точки на графіку
ax.scatter(x_rand, y_rand, s=1, c='blue', alpha=0.5)

plt.grid()
plt.show()