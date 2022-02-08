class fabricaTelefonos():
    marca = 'huawei'
    color = 'negro'
    memoriaRam = 32
    almacenamiento = 128
    
    def llamar(self , mensaje): #(parametro , argumento)
        return mensaje
          #metodo de instancia: es un metodo de yo estoy creando, posse el paramtro self
    def escucharMusica(self):
        print('estas escuchando musica')


telefono = fabricaTelefonos()
print(telefono)

#colocar el atributo al objeto(telefono)
telefono.marca
print(telefono.marca)
telefono.color
telefono.memoriaRam
telefono.almacenamiento
print(telefono.almacenamiento)


print(telefono.llamar('holaaa'))
telefono.escucharMusica()


