
def leer(nombre):
    try:
        f=open(nombre, 'r')
    except FileNotFoundError:
        print('no existe el fichero')
    else:
        print(f.read())
        f.close()
    return


def escribir(nombre):
   #toma de datos  
    dni= input("Introduzca su dni:")
    mes= input("Introduzca el mes :")
    dia= input("Introduzca el dia:")
    hora= input("Introduzca la hora:")
    especialidad= input("Introduzca la especialidad:")
    #escribir en fichero
    citas=open(nombre, 'a+')
    citas.write(dni + ";" + mes + ";"+ dia + ";" + hora + ";"+ especialidad + "\n")
    citas.close
    return

def buscar(fichero):
    dni2=input("Introduzca el DNI de la Cita:")
    with open(fichero, 'r') as f:
        for linea in f:
            if dni2 in linea:
                print(linea)
    return

def eliminar (fichero):
    dni=input("introduzca el Dni a Eliminar:")
    d=leer(fichero)
    with open(fichero, 'w') as f:
        for linea in d:
            if dni not in linea:
                f.write(linea)
    return


def menu():
    print("============================")
    print("Aplicacion Banco de Negreira")
    print("============================")
    print("1 - Consultar Citas")
    print("2 - Añadir cita nueva")
    print("3 - Buscar una Cita")
    print("4 - Eliminar Citas")
    print("0 - Salir")

    op=input("Introduzca La Opcion Deseada:")
    return op



def gestion():
    fichero="Banco.csv"
    while True:
        opcion=menu()
        if opcion == '1':
            leer(fichero)
        elif opcion == '2':
            escribir(fichero)
        elif opcion == '3':
            buscar(fichero)
        elif opcion == '4':
            eliminar(fichero)
        else:
            break

    
gestion()



