import math
import numpy
from scipy import integrate
from Form import Application


import tkinter as tk  # для интерфейса

# Функция formula() составляет latex-код наших формул
def formula(R):
    global form
    form.insert(0, r"$R_{k,1}=\frac{1}{2}[R_{k-1,1}+h_{k-1}\sum_{i=1}^{2^{k-2}}f(a+h_{k-1}(i-0.5))]$")
    form.insert(1, r"$R_{i,j}=[2^{2(j-1)}R_{i,j-1}-R_{i-1,j-1}]/(2^{2(j-1)}-1)$")
    form.append(r"Решение scipy: 0.484106269142131")
    form.append(rf"Моё решение ($R_{{{6,6}}}$): {R[6][6]}")
    form.append(rf"Моё решение ($R_{{{10,10}}}$): {R[10][10]}")
    root = tk.Toplevel()
    app = Application(form, master=root)
    app.mainloop()

# Функция colculation() высчитывает значение интеграла для нашего уравнения
def colculation():
    global form
    lstX = numpy.arange(0.4, 1.21, 0.02) # Лист из Xов
    lmd = lambda x: (math.sqrt(x) * math.cos(pow(x, 2))) # Лямбда-функция нашего интеграла
    lstY = list(map(lmd, lstX)) # Лист из Yов
    R = [[0 for i in range(len(lstX))] for i in range(len(lstX))]

    # Начало рассчётов
    R[1][1] = (lstX[-1] - lstX[0]) / 2 * (lstY[0] + lstY[-1])
    form.append(rf"$R_{{{1, 1}}}={R[1][1]}$")
    # Вначале рассчитаем R[k][1]
    for i in range(2, len(lstX)):
        buf = i - 2
        h = (lstX[-1] - lstX[0]) / math.pow(2, buf)
        Sum = 0
        Pred = math.pow(2, buf)
        for j in range(1, int(Pred) + 1):
            Sum += (math.sqrt(lstX[0] + h * (j - 0.5)) * math.cos(pow((lstX[0] + h * (j - 0.5)), 2)))
        R[i][1] = 0.5 * (R[i - 1][1] + h * Sum)
        form.append(rf"$R_{{{i,1}}}={R[i][1]}$")
        if (abs(R[i][1] - R[i - 1][1]) < 0.000005): # Какая точность будет
            break
    # Рассчитаем R[k][j]
    for i in range(2, len(lstX)):
        last = 1
        for j in range(2, i + 1):
            R[i][j] = (math.pow(2, (2 * (j - 1))) * R[i][j - 1] - R[i - 1][j - 1]) / (math.pow(2, (2 * (j - 1))) - 1)
            form[i-1] += rf" $R_{{{i,j}}}={R[i][j]}$"
            # form.insert(i-1, rf"$R_{{{i,j}}}={R[i][j]}$")
            last += 1
            if (abs(R[i][j] - R[j - 1][1]) < 0.000005): # Какая точность будет
                break
        if (abs(R[i][1] - R[i - 1][1]) < 0.000005): # Какая точность будет
            break
    formula(R)

form = [] # В структуре данных form будут хранится формулы и информация для вывода на экран
lmd = lambda x: (math.sqrt(x) * math.cos(pow(x, 2))) # Наш интерал в виде лямбда функции
result = integrate.romberg(lmd, 0.4, 1.2, show=True) # Решение интеграла по методу Ромберга с помощью библиотеки scipy
colculation()
