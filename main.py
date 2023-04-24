import matplotlib.pyplot as plt  # для графиков
import math
import numpy
from scipy import integrate
from Form import Application
from threading import Thread
from matplotlib.patches import Polygon
# Аппроксимация полиномиальной кривой с одной переменной


import tkinter as tk  # для интерфейса
from tkinter import ttk


# Функция formula() составляет latex-код наших формул
def formula(R):
    form = []
    form += [r"$R_{k,1}=\frac{1}{2}[R_{k-1,1}+h_{k-1}\sum_{i=1}^{2^{k-2}}f(a+h_{k-1}(i-0.5))]$"]
    form += [r"$R_{i,j}=[2^{2(j-1)}R_{i,j-1}-R_{i-1,j-1}]/(2^{2(j-1)}-1)$"]
    print(len(R))
    root = tk.Toplevel()
    app = Application(form, master=root)
    app.mainloop()


# Функция colculation(a) высчитывает значение интеграла для функции с индексом a
def colculation(a):
    if (a == 0):
        lstX = numpy.arange(0.8, 1.21, 0.02)
        lmd = lambda x: (1 / (math.sqrt(2 * pow(x, 2) + 1)))
        lstY = list(map(lmd, lstX))
        lstfullY = list(map(lmd, numpy.arange(0, 10, 0.02)))
        result = "{:.2f}".format(integrate.simpson([lmd(i) for i in lstX], dx=0.02))
        print(result)
        thread1 = Thread(target=lambda: Table(lstX, lstY, result, "scipy"))
        resultSvoi = 0
        resultSvoi += lstY[0]
        for i in range(1, len(lstY) - 1):
            if (i % 2 != 0):
                resultSvoi += 4 * lstY[i]
            else:
                resultSvoi += 2 * lstY[i]
        resultSvoi += lstY[-1]
        resultSvoi *= (0.02 / 3)
        resultSvoi = "{:.2f}".format(resultSvoi)
        print(resultSvoi)
        thread2 = Thread(target=lambda: Table(lstX, lstY, resultSvoi, "свои расчёты"))
        thread3 = Thread(target=lambda: draw(lstX, lstY, 0.8, 1.20, lstfullY))
        thread4 = Thread(target=lambda: formula(1))

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
    elif (a == 1):
        lstX = numpy.arange(0.4, 1.21, 0.02)
        lmd = lambda x: (math.cos(x) / (x + 1))
        lstY = list(map(lmd, lstX))
        lstfullY = list(map(lmd, numpy.arange(0, 10, 0.02)))
        result = "{:.2f}".format(integrate.simpson([lmd(i) for i in lstX], dx=0.02))
        print(result)
        thread1 = Thread(target=lambda: Table(lstX, lstY, result, "scipy"))
        resultSvoi = 0
        resultSvoi += lstY[0]
        for i in range(1, len(lstY) - 1):
            if (i % 2 != 0):
                resultSvoi += 4 * lstY[i]
            else:
                resultSvoi += 2 * lstY[i]
        resultSvoi += lstY[-1]
        resultSvoi *= (0.02 / 3)
        resultSvoi = "{:.2f}".format(resultSvoi)
        print(resultSvoi)
        thread2 = Thread(target=lambda: Table(lstX, lstY, resultSvoi, "свои расчёты"))
        thread3 = Thread(target=lambda: draw(lstX, lstY, 0.4, 1.20, lstfullY))
        thread4 = Thread(target=lambda: formula(1))

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
    elif (a == 2):
        lstX = numpy.arange(0.18, 0.99, 0.02)
        lmd = lambda x: (math.sin(2 * x) / (x + 1))
        lstY = list(map(lmd, lstX))
        lstfullY = list(map(lmd, numpy.arange(0, 10, 0.02)))
        result = "{:.2f}".format(integrate.simpson([lmd(i) for i in lstX], dx=0.02))
        print(result)
        thread1 = Thread(target=lambda: Table(lstX, lstY, result, "scipy"))
        resultSvoi = 0
        resultSvoi += lstY[0]
        for i in range(1, len(lstY) - 1):
            if (i % 2 != 0):
                resultSvoi += 4 * lstY[i]
            else:
                resultSvoi += 2 * lstY[i]
        resultSvoi += lstY[-1]
        resultSvoi *= (0.02 / 3)
        resultSvoi = "{:.2f}".format(resultSvoi)
        print(resultSvoi)
        thread2 = Thread(target=lambda: Table(lstX, lstY, resultSvoi, "свои расчёты"))
        thread3 = Thread(target=lambda: draw(lstX, lstY, 0.18, 0.98, lstfullY))
        thread4 = Thread(target=lambda: formula(1))

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
    elif (a == 3):
        lstX = numpy.arange(1, 2.01, 0.02)
        lmd = lambda x: (1 / (math.sqrt(2 * pow(x, 2) + 1.3)))
        lstY = list(map(lmd, lstX))
        lstfullY = list(map(lmd, numpy.arange(0, 10, 0.02)))
        result = "{:.2f}".format(integrate.simpson([lmd(i) for i in lstX], dx=0.02))
        print(result)
        thread1 = Thread(target=lambda: Table(lstX, lstY, result, "scipy"))
        resultSvoi = 0
        resultSvoi += lstY[0]
        for i in range(1, len(lstY) - 1):
            if (i % 2 != 0):
                resultSvoi += 4 * lstY[i]
            else:
                resultSvoi += 2 * lstY[i]
        resultSvoi += lstY[-1]
        resultSvoi *= (0.02 / 3)
        resultSvoi = "{:.2f}".format(resultSvoi)
        print(resultSvoi)
        thread2 = Thread(target=lambda: Table(lstX, lstY, resultSvoi, "свои расчёты"))
        thread3 = Thread(target=lambda: draw(lstX, lstY, 1, 2, lstfullY))
        thread4 = Thread(target=lambda: formula(1))

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
    elif (a == 4):
        lstX = numpy.arange(0.8, 1.21, 0.02)
        lmd = lambda x: (math.cos(x) / (pow(x, 2) + 1))
        lstY = list(map(lmd, lstX))
        lstfullY = list(map(lmd, numpy.arange(0, 10, 0.02)))
        result = "{:.2f}".format(integrate.simpson([lmd(i) for i in lstX], dx=0.02))
        print(result)
        thread1 = Thread(target=lambda: Table(lstX, lstY, result, "scipy"))
        resultSvoi = 0
        resultSvoi += lstY[0]
        for i in range(1, len(lstY) - 1):
            if (i % 2 != 0):
                resultSvoi += 4 * lstY[i]
            else:
                resultSvoi += 2 * lstY[i]
        resultSvoi += lstY[-1]
        resultSvoi *= (0.02 / 3)
        resultSvoi = "{:.2f}".format(resultSvoi)
        print(resultSvoi)
        thread2 = Thread(target=lambda: Table(lstX, lstY, resultSvoi, "свои расчёты"))
        thread3 = Thread(target=lambda: draw(lstX, lstY, 0.8, 1.20, lstfullY))
        thread4 = Thread(target=lambda: formula(1))

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
    elif (a == 5):
        lstX = numpy.arange(0.8, 1.61, 0.02)
        lmd = lambda x: ((pow(x, 2) + 1) * math.sin(x - 0.5))
        lstY = list(map(lmd, lstX))
        lstfullY = list(map(lmd, numpy.arange(0, 10, 0.02)))
        result = "{:.2f}".format(integrate.simpson([lmd(i) for i in lstX], dx=0.02))
        print(result)
        thread1 = Thread(target=lambda: Table(lstX, lstY, result, "scipy"))
        resultSvoi = 0
        resultSvoi += lstY[0]
        for i in range(1, len(lstY) - 1):
            if (i % 2 != 0):
                resultSvoi += 4 * lstY[i]
            else:
                resultSvoi += 2 * lstY[i]
        resultSvoi += lstY[-1]
        resultSvoi *= (0.02 / 3)
        resultSvoi = "{:.2f}".format(resultSvoi)
        print(resultSvoi)
        thread2 = Thread(target=lambda: Table(lstX, lstY, resultSvoi, "свои расчёты"))
        thread3 = Thread(target=lambda: draw(lstX, lstY, 0.8, 1.60, lstfullY))
        thread4 = Thread(target=lambda: formula(1))

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
    elif (a == 6):
        lstX = numpy.arange(2, 3.51, 0.02)
        lmd = lambda x: (1 / (math.sqrt(pow(x, 2) - 1)))
        lstY = list(map(lmd, lstX))
        lstfullY = list(map(lmd, numpy.arange(1.01, 10, 0.02)))
        result = "{:.2f}".format(integrate.simpson([lmd(i) for i in lstX], dx=0.02))
        print(result)
        thread1 = Thread(target=lambda: Table(lstX, lstY, result, "scipy"))
        resultSvoi = 0
        resultSvoi2 = ((3 * 0.02) / (8)) * (lstY[0] + 3 * lstY[1] + 3 * lstY[2] + lstY[3])
        for i in range(4, len(lstY) - 5):
            if (i % 2 != 0):
                resultSvoi += 4 * lstY[i]
            else:
                resultSvoi += 2 * lstY[i]
        resultSvoi += lstY[-1]
        resultSvoi *= (0.02 / 3)
        resultSvoi += resultSvoi2
        resultSvoi = "{:.2f}".format(resultSvoi)
        print(resultSvoi)
        thread2 = Thread(target=lambda: Table(lstX, lstY, resultSvoi, "свои расчёты"))
        thread3 = Thread(target=lambda: draw(lstX, lstY, 2, 3.50, lstfullY))
        thread4 = Thread(target=lambda: formula(2))

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
    elif (a == 7):
        lstX = numpy.arange(0.4, 1.21, 0.02)
        lmd = lambda x: (math.sqrt(x) * math.cos(pow(x, 2)))
        lstY = list(map(lmd, lstX))
        lstfullY = list(map(lmd, numpy.arange(0, 10, 0.02)))
        result = "{:.2f}".format(integrate.simpson([lmd(i) for i in lstX], dx=0.02)) # Решение через scipy
        thread1 = Thread(target=lambda: Table(lstX, lstY, result, "scipy")) # Вывод таблицы с решением через scipy
        R = [[0 for i in range(len(lstX))] for i in range(len(lstX))]

        R[1][1] = (lstX[-1]-lstX[0])/2*(lstY[0]+lstY[-1])
        for i in range(2, len(lstX)):
            buf = i-2
            h = (lstX[-1]-lstX[0])/math.pow(2, buf)
            Sum = 0
            Pred = math.pow(2, buf)
            for j in range(1, int(Pred)+1):
                Sum += (math.sqrt(lstX[0]+h*(j-0.5)) * math.cos(pow((lstX[0]+h*(j-0.5)), 2)))
            R[i][1] = 0.5*(R[i-1][1]+h*Sum)
            if (abs(R[i][1] - R[i - 1][1]) < 0.000005):
                break
        for i in range(2, len(lstX)):
            last = 1
            for j in range(2, i+1):
                R[i][j] = (math.pow(2, (2*(j-1)))*R[i][j-1]-R[i-1][j-1])/(math.pow(2, (2*(j-1)))-1)
                last += 1
                if (abs(R[i][j] - R[j - 1][1]) < 0.000005):
                    break
            if (abs(R[i][1] - R[i - 1][1]) < 0.000005):
                break
        for i in range(1, last+1):
            for j in range(1, i+1):
                print(R[i][j], sep=" ")
            print()
        print(R)
        formula(R)
    elif (a == 8):
        lstX = numpy.arange(0.8, 1.21, 0.02)
        lmd = lambda x: (math.sin(pow(x, 2) - 0.4) / (x + 2))
        lstY = list(map(lmd, lstX))
        lstfullY = list(map(lmd, numpy.arange(0, 10, 0.02)))
        result = "{:.2f}".format(integrate.simpson([lmd(i) for i in lstX], dx=0.02))
        print(result)
        thread1 = Thread(target=lambda: Table(lstX, lstY, result, "scipy"))
        resultSvoi = 0
        resultSvoi += lstY[0]
        for i in range(1, len(lstY) - 1):
            if (i % 2 != 0):
                resultSvoi += 4 * lstY[i]
            else:
                resultSvoi += 2 * lstY[i]
        resultSvoi += lstY[-1]
        resultSvoi *= (0.02 / 3)
        resultSvoi = "{:.2f}".format(resultSvoi)
        print(resultSvoi)
        thread2 = Thread(target=lambda: Table(lstX, lstY, resultSvoi, "свои расчёты"))
        thread3 = Thread(target=lambda: draw(lstX, lstY, 0.8, 1.20, lstfullY))
        thread4 = Thread(target=lambda: formula(1))

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
    elif (a == 9):
        lstX = numpy.arange(0.2, 1.01, 0.02)
        lmd = lambda x: ((x + 1) * math.cos(pow(x, 2)))
        lstY = list(map(lmd, lstX))
        lstfullY = list(map(lmd, numpy.arange(0, 10, 0.02)))
        result = "{:.2f}".format(integrate.simpson([lmd(i) for i in lstX], dx=0.02))
        print(result)
        thread1 = Thread(target=lambda: Table(lstX, lstY, result, "scipy"))
        resultSvoi = 0
        resultSvoi += lstY[0]
        for i in range(1, len(lstY) - 1):
            if (i % 2 != 0):
                resultSvoi += 4 * lstY[i]
            else:
                resultSvoi += 2 * lstY[i]
        resultSvoi += lstY[-1]
        resultSvoi *= (0.02 / 3)
        resultSvoi = "{:.2f}".format(resultSvoi)
        print(resultSvoi)
        thread2 = Thread(target=lambda: Table(lstX, lstY, resultSvoi, "свои расчёты"))
        thread3 = Thread(target=lambda: draw(lstX, lstY, 0.2, 1, lstfullY))
        thread4 = Thread(target=lambda: formula(1))

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()

# Функция Table(lstX, lstY, integral, method) формирует таблицу со значениями x, y,
# интеграла и каким методом мы его вычислили (самостоятельно или scipy)
def Table(lstX, lstY, integral, method):
    root1 = tk.Tk()
    root1.geometry("700x500")
    game_frame = tk.Frame(root1)
    game_frame.pack()
    # скроллбар
    game_scroll = tk.Scrollbar(game_frame, orient='vertical')
    game_scroll.pack(side="right", fill="y")
    my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set, height=15)

    my_game.pack()

    game_scroll.config(command=my_game.yview)

    my_game['columns'] = ('X', 'Y')

    # Форматируем колонки
    my_game.column("#0", width=0, stretch='no')
    my_game.column("X", anchor='center', width=150)
    my_game.column("Y", anchor='center', width=150)

    # Создаём имена для колонок
    my_game.heading("#0", text="", anchor='center')
    my_game.heading("X", text="X", anchor='center')
    my_game.heading("Y", text="Y", anchor='center')

    # Заполняем таблицу данными
    for i in range(len(lstX)):
        my_game.insert(parent='', index='end', iid=i, text='',
                       values=("{:.2f}".format(lstX[i]), "{:.2f}".format(lstY[i])))

    my_game.pack()
    text = tk.Label(root1, text=f'Значение интеграла: {integral} и каким методом он посчитан {method}')
    text.pack()

    root1.mainloop()

# Функция HelloWidget() - приветственная функция, которая предлагает пользователю выбрать из 10 функций одну на вычисление интеграла
def HelloWidget():
    root1 = tk.Tk()
    root1.geometry("900x550")
    photo = []
    for i in range(1, 11):
        a = str(i)
        photo.append(tk.PhotoImage(file=rf"img{a}.png"))
    tk.Button(root1,
              text='Y',
              image=photo[0],
              command=lambda: colculation(0),
              # command=root1.quit,
              font=("Helvetica 11")).place(x=(25 + 0 * 180), y=50)
    tk.Button(root1,
              text='Y',
              image=photo[1],
              command=lambda: colculation(1),
              # command=root1.quit,
              font=("Helvetica 11")).place(x=(25 + 1 * 180), y=50)
    tk.Button(root1,
              text='Y',
              image=photo[2],
              command=lambda: colculation(2),
              # command=root1.quit,
              font=("Helvetica 11")).place(x=(25 + 2 * 180), y=50)
    tk.Button(root1,
              text='Y',
              image=photo[3],
              command=lambda: colculation(3),
              # command=root1.quit,
              font=("Helvetica 11")).place(x=(25 + 0 * 180), y=150)
    tk.Button(root1,
              text='Y',
              image=photo[4],
              command=lambda: colculation(4),
              # command=root1.quit,
              font=("Helvetica 11")).place(x=(25 + 1 * 180), y=150)
    tk.Button(root1,
              text='Y',
              image=photo[5],
              command=lambda: colculation(5),
              # command=root1.quit,
              font=("Helvetica 11")).place(x=(25 + 2 * 180), y=150)
    tk.Button(root1,
              text='Y',
              image=photo[6],
              command=lambda: colculation(6),
              # command=root1.quit,
              font=("Helvetica 11")).place(x=(25 + 0 * 180), y=250)
    tk.Button(root1,
              text='Y',
              image=photo[7],
              command=lambda: colculation(7),
              # command=root1.quit,
              font=("Helvetica 11")).place(x=(25 + 1 * 180), y=250)
    tk.Button(root1,
              text='Y',
              image=photo[8],
              command=lambda: colculation(8),
              # command=root1.quit,
              font=("Helvetica 11")).place(x=(25 + 2 * 180), y=250)
    tk.Button(root1,
              text='Y',
              image=photo[9],
              command=lambda: colculation(9),
              # command=root1.quit,
              font=("Helvetica 11")).place(x=25, y=350)

    tk.mainloop()


# Функция draw рисует кривую и закрашенную область под ней на координатной плоскостях
def draw(ix, iy, a, b, yF):
    x = numpy.arange(0, 10, 0.02)
    y = yF

    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=2)
    ax.set_ylim(bottom=0)

    # Make the shaded region
    verts = [(a, 0), *zip(ix, iy), (b, 0)]
    poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
    ax.add_patch(poly)

    fig.text(0.9, 0.05, '$x$')
    fig.text(0.1, 0.9, '$y$')

    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    ax.xaxis.set_ticks_position('bottom')

    ax.set_xticks([a, b], labels=['$a$', '$b$'])
    ax.set_yticks([])

    plt.show()


# HelloWidget()
colculation(7)
# for i in range(1, 2):
#     print(i)