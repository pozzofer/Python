'''class fabricaTelefonos():
    marca = 'samsung'

    def elaborarHuawei(self):
        self.marca = 'Huawei' #para que reconozca la marca adentro del metodo se le puso <self.> antes de <marca>

telefono = fabricaTelefonos()
print(telefono.marca)
 
telefono.elaborarHuawei()      
print(telefono.marca) 
       '''
#metodo init sirve para ejecutarse al iniciar el objeto

class fabricaTelefonos():
    def __init__(self , marca , color):
        self.marca =marca
        self.color = color #aqui se colocan los atributos
        print('estoy ejecutando el metodo init porque se ha creado un nuevo objeto')

telefono = fabricaTelefonos('huawei' , 'negro')
print('el celular es de la marca' , telefono.marca)
print('el color del celular sera' , telefono.color)