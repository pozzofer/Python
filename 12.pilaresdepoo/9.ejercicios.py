'''Realizar un programa que conste de una clase llamada Estudiante, 
que tenga como atributos el nombre y la nota del alumno.
 Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el
  resultado de la nota y si ha aprobado o no.'

class Estudiante():
    def __init__(self , nombre , nota):
        self.nombre = nombre
        print ("nombre: ", self.nombre)
        self.nota = nota
        print("nota: " , self.nota)
        if self.nota >= 7: 
            print("el alumno {} ha aprobado".format(self.nombre))
            
        else:
            print("el alumno ha desaprobado")   

Alumno = Estudiante('matias', 5)'''


# Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; 
# luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro.
#  Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. 
# Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno

# class Fabrica():
#     def __init__(self , llantas , color , precio):
#         self.llantas = llantas
#         self.color = color
#         self.precio = precio
#         print("estoy fabricando weas") 

# class Moto(Fabrica):
#     def __init__(self , llantas , color , precio):
#           super().__init__(llantas , color , precio)

# class Auto(Fabrica):
#     pass


# moto = Moto("2" , "rojo" , "$5")
# print(moto.llantas)
# print(moto.color)
# print(moto.precio)

# auto = Auto("4" , "blanco" , "$55")
# print(auto.llantas)
# print(auto.color)
# print(auto.precio)


# Crear una clase llamada Marino(), con un metodo que sea hablar, en donde muestre un mensaje que diga 
# "Hola...". Luego, crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar por 
# "Soy un Pulpo". Por ultimo, crear una clase Foca(), heredada de Marino,
#  pero que tenga un atributo nuevo llamado mensaje y que muestre ese mesjae como parametro

# class Marino():
#     def __init__(self , hablar):
#         self.hablar = hablar

# marino = Marino("ola")        
# print(marino.hablar) 

# class Pulpo(Marino):
#     pass

# pulpo = Pulpo("soy un pulpo")
# print(pulpo.hablar)     

# class Foca(Marino):
#     def __init__(self , mensaje):
#         self.mensaje = mensaje
#         print(self.mensaje)

# foca = Foca("me fui a mundo marino")  
# foca.mensaje      


# Crear un programa con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). 
# Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante).
#  Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe imprimir la especialidad, 
# edad, nombre y universidad de dicho estudiante con un objeto llamado persona.

class Universidad():
    def __init__(self , nombreUniversidad):
        self.nombreUniversidad = nombreUniversidad
        print("Universidad : {}".format(self.nombreUniversidad))


class Carrera():
    def __init__(self , especialidad):
        self.especialidad = especialidad
        print("especialidad : {} ".format(self.especialidad) )

class Estudiante():
    def __init__(self , nombre , edad):
        self.nombre = nombre
        self.edad = edad
        print("Nombre del Alumno: {}".format(self.nombre) , "\n Edad: {}".format(self.edad))


class Persona(Universidad , Carrera , Estudiante):
    pass

persona = Persona("UBA" , "Psicologia" , "fernanda" , "22")
persona = Persona("UBA")
print(persona.nombreUniversidad())
persona = Persona("Psicologia")               #revisar usar return!!!!!!!!!!!!!!!!!!!
print(persona.especialidad())
persona = Persona("fernanda" , "22")
print(persona.nombre())
print(persona.edad())