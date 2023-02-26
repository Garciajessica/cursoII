
import json
'''
Crear un programa que permita emular el almacenamiento de usuarios en una base de datos 
'''
'''UsuarioyContrasena = {}
datos = 'si'
while datos:
    usuario = input('Ingrese el usuario')
    contrasena = input('ingrese su contrasena')
    
    UsuarioyContrasena[usuario]= contrasena
    
    print(UsuarioyContrasena)
 '''   
'''Menu'''

opcion = int(input('Bienvenido! n/Selecciona la opcion deseada: /n1)Registrar usuario /n2-Mosrar informacion de usuarios'))




f = open('/Users/jessicadahianagarcia/Desktop/Proyecto Python/primeraPre-entrega/basededatos.txt', 'w')

def basededatos():

    UsuarioyContrasena = {}
    datos = 0
    while datos:
     usuario = input('Ingrese el usuario: ')
     contrasena = input('ingrese su contrasena: ')
     
     UsuarioyContrasena[usuario]= contrasena
     continue

    
f.close()



f = open("BDJSON", "r")
json.load

'''
Crear inputs para el usuario y contrasena
'''

        
    
'''
    funcion para almacenar informacion y otra para mostrar
'''
    
    
  
    
    
'''
    Funcion para el login de usuario y comprobar que la contrasena coincide
    con el usuario  mostrando un mensaje de bienvenida y en caso contrario 
    mostrar un error 
'''
