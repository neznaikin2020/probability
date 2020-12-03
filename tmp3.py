from collections import Counter # Не загружается по умолчанию
import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt,pi,e
# создаем список из файла
dir = r"C:\exportAllIN.txt"
with open(dir) as file:
    array = [row.strip() for row in file]
# преобразуем список в массив чисел
data = np.array(array)
data.reshape(1,len(array))
# преобразуем во float
data = data.astype("float")
# группируем данные, определяем частоту
print(data)
count_data = Counter(data)
# строим диаграмму
xs = count_data.keys()
ys = count_data.values()
plt.bar(xs, ys)
plt.title ("Гистограмма нашего распределения")
plt.xlabel("Время")
plt.ylabel("Частота")
plt.show()
print("Математическое ожидание по выборке(общее для сравниваемых распределений) -%s"%str(round(np.mean(data),3)))
print("СКО по выборке(общее для сравниваемых распределений) -%s"%str(round(np.std(data),3)))
print("Энтропийное значение погрешности-%s"%str(round(np.std(data)*sqrt(np.pi*np.e*0.5),3)))
#print(count_data)
#print(data)
from scipy.stats import logistic,uniform,norm,pearsonr

import numpy as np
import matplotlib.pyplot as plt0
import pandas as pd
fig, ax = plt0.subplots(1, 1)
n=len(data)# объём выборки
x=uniform.rvs(loc=0, scale=n, size=n)#равномерное распределение
x.sort()#сортировка
pu=uniform.cdf(x/(np.max(x)))#равномерное интегральное  распределение
ax.plot(x,pu, lw=5, alpha=0.6, label='uniform cdf')
pn=norm.cdf(x, np.mean(x), np.std(x))#нормальное интегральное  распределение
ax.plot(x,pn, lw=5, alpha=0.6, label='norm cdf')
pl=logistic.cdf(x, np.mean(x), np.std(x))# логистическое  интегральное  распределение
ax.plot(x,pl, lw=5, alpha=0.6, label='logistic cdf')
p=np.arange(0,len(x),1)/len(x)
ax.plot(x,p, lw=5, alpha=0.6, label='test')
ax.legend(loc='best', frameon=False)
print("Как на этот же график вывести плотность функции data???")
plt0.show()

from pydoc import help
from scipy.stats.stats import pearsonr
#help(pearsonr)
def getres(data1,data2, s):
    r, p = pearsonr(data1, data2)
    print("=================================")
    print("Сравниваемое распределение -", s)
    print("Коэффициент корреляции Пирсона", r)
    print("P-значение", p)
    print("=================================")
#    return r,p
getres(data,x, "равномерное")
getres(data,pu, "равномерное интегральное  распределение")
getres(data,pn, "нормальное интегральное  распределение")
getres(data,pl, "логистическое  интегральное  распределение")


from scipy import stats
a = np.array([0, 0, 0, 1, 1, 1, 1])
b = np.arange(7)
print(stats.pearsonr(a, b))
getres(a,b, "a и b")