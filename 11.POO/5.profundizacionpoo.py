class fabricaTelefonos():
    def __init__(self , marca , *colores , **modelos):
        self.marca = marca
        self.colores = colores
        self.modelos = modelos 
telefono = fabricaTelefonos('alcatel' , 'rojo' , 'negro' , m1 = 500 , m2 = 1000)
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)

#atributos temporales
telefono.memoria = 512
print(telefono.memoria)