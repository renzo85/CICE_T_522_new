# Esta actividad tendrá como objetivo procesar y analizar los casos confirmados de covid-19 por municipios
# https://datos.comunidad.madrid/catalogo/dataset/7da43feb-8d4d-47e0-abd5-3d022d29d09e/resource/ead67556-7e7d-45ee-9ae5-68765e1ebf7a/download/covid19_tia_muni_y_distritos.json

# Considerar que los datos van desde 26-FEB-2020 hasta 1-JUL-2020 y hasta esta fecha se subían de manera diaria

# 1.Cantidad total de municipios

# 2.confirmados totales a 26-FEB-2020

# 3.confirmados totales a 1-JUL-2020

# 4.Obtener los 10 municipios con mayor cantidad de confirmados totales

# 5.Crear una lista con la sumatoria de los casos confirmados totales por día

# 6.Crear un objeto estadística que reciba un valor X y otro valor Y, deben ser listas

# 7.Agregar las siguientes propiedades:

# 8.Obtener n

# 9.Media X e Y

# 10.Varianza_x: Σ(Xⁱ - |X) / n

# 11.Varianza_y: Σ(Yⁱ - |Y) / n

# 12.Covarianza: (ΣXY / n) - |X|Y

# 13.rxy = Sxy / (Sx*Sy)

# 14.B = rxy * (Sy/Sx)

# 15.B0 = |Y - B|X

# 16.Puntuación directa: Y' = BXⁱ + B0

# 17.Cuántos confirmados tendremos el 1 de agosto del año 2020?

#----------------------------------

import funcs
import time
from std import Statistics

# 1.Cantidad total de municipios

print("Cantidad total de municipios es "+ str(funcs.get_muni(funcs.data)))

# 2.confirmados totales a 26-FEB-2020

date = "2020/02/26"
print("Confirmados totales a 26-FEB-2020 es " + str(funcs.get_ccdate(funcs.data, date)))

# 3.confirmados totales a 1-JUL-2020

date = "2020/07/01"
print("Confirmados totales a 1-JUL-2020 es " + str(funcs.get_ccdate(funcs.data, date)))

# 4.Obtener los 10 municipios con mayor cantidad de confirmados totales

print("10 municipios con mayor cantidad de confirmados totales:")
print(funcs.top_ten(funcs.data))

# 5.Crear una lista con la sumatoria de los casos confirmados totales por día

start = time.perf_counter()
Y = funcs.sum_tot_dia(funcs.data)
print (Y)
finish = time.perf_counter()
print(finish - start)

Y = dict(sorted(Y.items(), key= lambda tupla: tupla[0]))
#X = list(Y.keys())
Y = list(Y.values())
X = []
for num in range(1, len(Y) + 1): #se le aumenta 1 porque no incluía el último número
    X.append(num)
print(Y, X)

# 6.Crear un objeto estadística que reciba un valor X y otro valor Y, deben ser listas

covid_data = Statistics(X, Y)

# 7.Agregar las siguientes propiedades:

# 8.Obtener n
print (covid_data.n)

# 9.Media X e Y
print (covid_data.x_mean)
print (covid_data.y_mean)

# 10.Varianza_x
print(covid_data.x_var)

# 11.Varianza_y
print(covid_data.y_var)

# 12.Covarianza
print(covid_data.cov)

# 13.Coeficiente de correlación entre x e y
print (covid_data.cor)

#14. Pendiente de la recta
print (covid_data.pend)

# 15.B0
print (covid_data.B0)

