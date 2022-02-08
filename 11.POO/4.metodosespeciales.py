#metodo init metodo constructor
class fabricaTelefonos():
    def __init__(self , marca , color):
        self.marca = marca
        self.color = color 
        print('el objeto {} ha sido creado'.format(self.marca))

    #metodo str    
    def __str__(self):
        return "el objeto es {}".format(self.marca)
        #asicomo hay un costructor, tambien hay un destructor
    def __del__(self):
        print('el objeto {} ha sido destruido'.format(self.marca))    

telefono = fabricaTelefonos('nokia' , 'negro')
print(telefono.marca)        
print(telefono)



'''
un constructor se encarga de crear y setear los atributos de una sola vez
un destructor es un metodo que se ejecuta al finalizar la ejecucion de un programa que tiene clases y objetos y se encarga de
eliminar o erradicar a todos los objetos una vez finalizada la ejecucion del codigo'''
