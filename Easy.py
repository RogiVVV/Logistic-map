import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

# 2 - Параметр r влияет на высоту вершины параболы f(x) = rx(1-x) и на её ширину
xn = np.linspace(0, 1, 400)
for r in [0.5, 1, 1.5, 2.5, 3.0, 3.5, 4]:
    yn = r * xn * (1 - xn)
    plt.plot(xn, yn, label=f"r = {r}")

plt.xlabel("x_n")
plt.ylabel("x_{n+1}")
plt.legend()
plt.grid(True)
plt.show()

# 3
xn = np.linspace(0, 1, 400)
for r in [0.5, 1, 1.5, 27 / (2 * (7 * sqrt(7) - 10))]:
    yn = r * xn * (1 - xn) * (2 + xn)
    plt.plot(xn, yn, label=f"r = {r}")

plt.xlabel("x_n")
plt.ylabel("x_{n+1}")
plt.legend()
plt.grid(True)
plt.show()

# Вывод:
# Схожесть:
# 1) Это две одномерные параметрические функции
# 2) При малых r парабола расширяется
# Различия:
# 1) В логистическом отображении степень многочлена - 2, а в точечном - 3
# 2) Разная область значений параметра r
