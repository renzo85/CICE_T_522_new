
# 6.Crear un objeto estadística que reciba un valor X y otro valor Y, deben ser listas

class Statistics:
    def __init__(self, x, y):
        self.x = x if type(x) == list else []
        self.y = y if type(y) == list else []
        #el self n no lo pongo aquí porque se ejecutaría de forma estática y no se actualizaría conforme los valores de x que yo añada. Por eso lo uso como decorador de propiedad


# 7.Agregar las siguientes propiedades:

# 8.Obtener n

    @property #uso de decorador
    def n(self): #solo cuando sea él mismo, no le puedo añadir otro valor
        return len(self.x)

# 9.Media X e Y

    @property
    def x_mean(self):
        return sum(self.x)/self.n

    @property
    def y_mean(self):
        return sum(self.y)/self.n

# 10.Varianza_x

    @property
    def x_var(self):
        count = 0
        for num in self.x:
            count += ((num - self.x_mean) ** 2)
        x_var = count/self.n
        return x_var

# 11.Varianza_y

    @property
    def y_var(self):
        count = 0
        for num in self.y:
            count += ((num - self.y_mean) ** 2)
        y_var = count/self.n
        return y_var

# 12.Covarianza

    @property
    def xy(self):
        xy = sum([tupla[0] * tupla[1] for tupla in zip(self.x,self.y)]) #zip sirve para formar las tuplas de clave valor entre x e y
        return xy

    @property
    def cov(self):
        return (self.xy /self.n) - (self.x_mean * self.y_mean)


# 13.Coeficiente de correlación entre x e y

    @property
    def cor(self):
        return self.cov / ((self.x_var ** 0.5) * (self.y_var ** 0.5))

#14. Pendiente de la recta

    @property
    def pend(self):
        return self.cor / ((self.y_var ** 0.5) / (self.x_var ** 0.5))

# 15.B0

    @property
    def B0(self):
        return self.y_mean - (self.pend * self.x_mean)

# 16.Puntuación directa: Y' = BXⁱ + B0

    def prediction(self, value):
        return (self.pend * value) + self.B0



subject_1 = Statistics([1,2,3], [4,5,6])
print (subject_1.x_mean)

print (subject_1.x_mean)
print (subject_1.x_var)
print (subject_1.y_var)
print(subject_1.cov)
print(subject_1.cor)
print(subject_1.pend)
print(subject_1.B0)
print(subject_1.prediction(4))