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

class Statistics:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #el self n no lo pongo aquí porque se ejecutaría de forma estática y no se actualizaría conforme los valores de x que yo añada. Por eso lo uso como decorador de propiedad

    @property #uso de decorador
    def n(self): #solo cuando sea él mismo, no le puedo añadir otro valor
        return len(self.x)

    def x_mean(self):
        return sum(self.x)/self.n

subject_1 = Statistics([20,18,18,16], [1,2,3,4] )
print (subject_1.x_mean())
subject_1.x.append(19)
print (subject_1.x_mean())

#----------------------------------

import funcs
import time

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
print(funcs.sum_tot_dia(funcs.data))
finish = time.perf_counter()
print(finish - start)