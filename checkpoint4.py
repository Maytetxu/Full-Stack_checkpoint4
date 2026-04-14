#Ejercicio 1: lista, tuple, float, integer, decimal and dictionary

from decimal import Decimal
codigo_producto = ["01BD4", "05CD1", "04AC6", "08CD02"] #list
cliente = ("name", "adress", "cif_empresa") #tuple
productos = {                                    #dictionary
    "alimentacion" : ["embutidos", "pan", "frutas"],
    "bebidas" : ["zumo_mango", "zumo_naranja"],
    "lácteos" : ["queso", "yogur", "leche"],
}
coste_envio = 4
comision_envio = 0.05 #float
cantidad_envios = 16  #integer
coste_envio = Decimal (4)
comision_envio = Decimal(0.05)
cantidad_envios = Decimal(16)
total_comision = ((coste_envio * comision_envio) * (cantidad_envios))
print (total_comision) #3.2 decimal

 
#Ejercicio 2: Redondeo a enteros
import math
print (math.ceil (total_comision)) #3.2 redondeado hacia arriba = 4 

#Ejercicio 3: Raíz cuadrada
print (math.sqrt (comision_envio)) #0.22360679774997896

#Ejercicio 4: Slices in dictionary
productos = {                                    
    "alimentacion" : ["embutidos", "pan", "frutas"],
    "bebidas" : ["zumo_mango", "zumo_naranja"],
    "lácteos" : ["queso", "yogur", "leche"],
}
insumos_básicos = productos ["alimentacion"]
print (insumos_básicos)

#Ejercicio 5: Slices in tuples
cliente = ("name", "adress", "cif_empresa")
print (cliente [1])

#Ejercicio 6: Add elements in list using .extend
codigo_producto = ["01BD4", "05CD1", "04AC6", "08CD02"]
codigo_producto.extend (["09GN21"])
print (codigo_producto)

#Ejercicio 7: Replace the first element in your list
codigo_producto = ["01BD4", "05CD1", "04AC6", "08CD02", "09GN21"]
codigo_producto [0] = "02BE3"
print (codigo_producto)

#Ejercicio 8: Ordenar lista alfabéticamente
codigo_producto = ['02BE3', '05CD1', '04AC6', '08CD02', '09GN21']
codigo_producto.sort()
print (codigo_producto)

#Ejercicio 9: Usar reasignamiento a tupla
cliente = ("name", "adress", "cif_empresa")
print(id(cliente)) #ID=4505861888
cliente = cliente + ("contacto",)
cliente += ("contacto",)
print (cliente)
print(id(cliente)) #ID=4506161840
