import numpy as np
import random

def seleccion_menu():
   while True:
    opciones=input("Eliga una opción del menu.\n")
    if opciones.isdigit():
        opciones=int(opciones)
        return opciones
    else:

        print("Ingrese una opcion valida\n")
        continue

def trabajadoresorden(i,j):
    if i == 0:
        print("", valor[i, j])
    elif i == 1:
        print("", valor[i, j])
    elif i == 2:
        print("", valor[i, j])
    elif i == 3:
        print("", valor[i, j])
    elif i == 4:
        print("", valor[i, j])
    elif i == 5:
        print("", valor[i, j])
    elif i == 6:
        print("", valor[i, j])
    
def menu():
    print("""                  Menu
        1. Asignación de sueldos aleatoria.
        2. Clasificar sueldos.
        3. Ver estadisticas.
        4. Reporte de sueldos.
        5. Salir""")
    

trabajadores = ["Juan Peréz", 
                "Maria Garcia", 
                "Carlos López", 
                "Ana Martínez", 
                "Pedro Rodríguez", 
                "Laura Hernández", 
                "Miguel Sánchez", 
                "Isabel Gómez", 
                "Francisco Díaz", 
                "Elena Fernández"]

valor=np.empty([10,1],dtype="object")
tr = 0
while True: 
    menu()
    opcion = seleccion_menu()
    if seleccion_menu == 1:
       for designacion in trabajadores:
            aleatoria = random.randint()
            if designacion==0:
                valor[0,tr]=aleatoria
            elif designacion==1:
                valor[1,tr]= aleatoria
            elif designacion==3:
                valor[2,tr]= aleatoria
                break
    elif seleccion_menu == 2:
       for i in range(tr,0):
            print("Trabajador:")
            for j in range(10,0):
                trabajadoresorden(i,j)
       print(f"{valor}")
    elif seleccion_menu ==3:
        print()
    elif seleccion_menu == 4:
        print()
    else:
        break



