import matplotlib.pyplot as plt
import numpy as np


# логистическое отображение
def f(r, x):
    return r * x * (1 - x)


def g(r, x):
    return r * x * (1 - x) * (2 + x)


# 4
def lamerey_two_trajectories(r, x0=0.2, eps=1e-5, n_steps=50):
    xs = np.linspace(0, 1, 400)
    fx = f(r, xs)

    plt.figure(figsize=(6, 6))
    plt.plot(xs, fx, 'k', label=r'$y = f(x)$')
    plt.plot(xs, xs, 'r--', label=r'$y = x$')

    # первая траектория: x0
    x, y = x0, 0
    for _ in range(n_steps):
        y_new = f(r, x)
        plt.plot([x, x], [y, y_new], 'b')
        plt.plot([x, y_new], [y_new, y_new], 'b')
        x, y = y_new, y_new

    # вторая траектория: y0 = x0 + eps
    y0 = x0 + eps
    x, y = y0, 0
    for _ in range(n_steps):
        y_new = f(r, x)
        plt.plot([x, x], [y, y_new], 'g')
        plt.plot([x, y_new], [y_new, y_new], 'g')
        x, y = y_new, y_new

    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel(r'$x_n$')
    plt.ylabel(r'$x_{n+1}$')
    plt.title(fr'Две лестницы Ламерея, r = {r}, $x_0,\ x_0+\varepsilon$')
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect('equal', 'box')
    plt.tight_layout()
    plt.show()


lamerey_two_trajectories(4)
'''График при r = 4 сильно отличается от графиков при r < 4
траектори практически с самого начала начинают расходиться и уже
очень скоро двигаются хаотчно. Наблюдается так называемый эффект бабочки'''


# 5
def bifurcation_diagram(x0=0.2, n_iter=1000, n_keep=100):
    xs_plot = []
    rs_plot = []
    r = 4
    r_inf = 3.5699456
    while r > 0:
        x = x0

        for _ in range(n_iter - n_keep):
            x = f(r, x)

        # сохраняем последние n_keep значений
        for _ in range(n_keep):
            x = f(r, x)
            xs_plot.append(x)
            rs_plot.append(r)
        r -= 0.001

    plt.figure(figsize=(8, 6))
    plt.axvline(r_inf, color='r', linestyle='--',
                label=fr'$r_\infty \approx {r_inf}$')
    plt.plot(rs_plot, xs_plot, ',', markersize=1, color='k')
    plt.xlabel(r'$r$')
    plt.ylabel(r'$x$')
    plt.title('Бифуркационная диаграмма логистического отображения')
    plt.xlim(1, 4)
    plt.ylim(0, 1)
    plt.grid(False)
    plt.tight_layout()
    plt.show()


bifurcation_diagram()
'''Мы наблюдаем бифуркацию: сначала отображение стремилось к одной точке,
потом к двум, четырём, восьми, а после r_inf начинается хаос - нельзя выделить
конкретную точку, к которой стремится отображение'''


# 6, 7
def zoom_bifurcation(r_min=3.7, r_max=3.9,
                     n_r=4000, n_iter=1500, n_keep=300):
    xs_plot = []
    rs_plot = []

    rs = np.linspace(r_min, r_max, n_r)

    for r in rs:
        x = np.random.rand()

        for _ in range(n_iter - n_keep):
            x = f(r, x)

        for _ in range(n_keep):
            x = f(r, x)
            xs_plot.append(x)
            rs_plot.append(r)

    if r_min == 3.7 and r_max == 3.9:
        r_n = 3.83
    else:
        r_n = (r_min + r_max) / 2

    plt.figure(figsize=(8, 6))
    plt.plot(rs_plot, xs_plot, ',', markersize=1, color='k')
    plt.axvline(3.83, color='r', linestyle='--',
                label=fr'$r_\infty \approx {r_n}$')
    plt.axvspan(3.828497, 3.841082, alpha=0.1, color='red',
                label=f'Окно периода 3: [{3.828497}, {3.841082}]')
    plt.axvspan(3.738176, 3.740942, alpha=0.1, color='blue',
                label=f'Окно периода 5: [{3.7381767}, {3.740942}]')
    plt.axvspan(3.626653, 3.630110, alpha=0.1, color='green',
                label=f'Окно периода 6: [{3.626653}, {3.630110}]')
    plt.xlabel(r'$r$')
    plt.ylabel(r'$x$')
    plt.title(fr'Окрестность $r \approx {r_n}$')
    plt.xlim(r_min, r_max)
    plt.ylim(0, 1)
    plt.legend()
    plt.grid(False)
    plt.tight_layout()
    plt.show()


zoom_bifurcation()

zoom_bifurcation(r_max=3.8, r_min=3.6)


# 9
def bifurcation_g(x0=0.2, r_min=0.0, r_max=27 / (2 * (7 * np.sqrt(7) - 10)),
                  n_r=4000, n_iter=1500, n_keep=300):
    rs = np.linspace(r_min, r_max, n_r)
    xs_plot = []
    rs_plot = []

    for r in rs:
        x = x0

        for _ in range(n_iter - n_keep):
            x = g(r, x)

        for _ in range(n_keep):
            x = g(r, x)
            if -2 <= x <= 1:
                xs_plot.append(x)
                rs_plot.append(r)

    plt.figure(figsize=(8, 6))
    plt.axvline(0.5, color='r', linestyle='--',
                label=r'граница устойчивости $x^* = 0$')
    plt.plot(rs_plot, xs_plot, ',', markersize=1, color='k')
    plt.xlabel(r'$r$')
    plt.ylabel(r'$x$')
    plt.title('Бифуркационная диаграмма для $g_r(x)=r x(1-x)(2+x)$')
    plt.legend()
    plt.grid(False)
    plt.tight_layout()
    plt.show()


def zoom_bifurcation_g(r_min, r_max,
                       n_r=4000, n_iter=1500, n_keep=400):
    rs = np.linspace(r_min, r_max, n_r)
    xs_plot = []
    rs_plot = []

    for r in rs:
        x = np.random.rand()
        for _ in range(n_iter - n_keep):
            x = g(r, x)
        for _ in range(n_keep):
            x = g(r, x)
            if -2 <= x <= 1:
                xs_plot.append(x)
                rs_plot.append(r)

    plt.figure(figsize=(8, 6))
    plt.plot(rs_plot, xs_plot, ',', markersize=1, color='k')
    plt.xlabel(r'$r$')
    plt.ylabel(r'$x$')
    plt.title(fr'Увеличение бифуркации, $r\in[{r_min},{r_max}]$')
    plt.legend()
    plt.grid(False)
    plt.tight_layout()
    plt.show()


bifurcation_g()

zoom_bifurcation_g(1.5, 1.6)
