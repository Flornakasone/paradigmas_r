# Todos los ejercicios deberán contener las validaciones y excepciones correspondientes.

# Usted ha sido contratado para desarrollar una solución que le permita al dpto. De RRHH obtener de manera ágil el estado de los gastos por viáticos. 

# La empresa tiene los datos de viáticos del mes en un archivo csv. El sistema deberá :
#a) Tener un menú de acciones 
#b) Permitir la carga de datos del legajo completo (legajo, apellido, nombre) y guardarlos en un archivo csv cuyo nombre será dado por el usuario. Si el archivo ya existe deberá preguntar si se desea agregar o sobreescribirlo. * sólo validar que Legajo  sea un entero
#c) Dado el número de legajo de un empleado calcular e informar en pantalla los gastos que hizo hasta el momento,  junto con el resto de sus datos. Si superó los $5000 indicar que se ha pasado del presupuesto y por cuanto. Por ejemplo "Legajo 1 : Laura Estebanez, gastó $9000 y se ha pasado del presupuesto por $4000" 
# Caso contrario solo mostrar:  "Legajo 1 : Laura Estebanez, gastó $488" 


# Tenga en cuenta que las acciones del menú no tienen un orden en particular.



import csv
import os.path

def validacion_int(str):
    try:
        entero = int(str)
        return True
    except ValueError:
        return False

def carga_datos(campos):
    guardar = "si"
    lista = []

    while guardar == "si":
        empleado ={}
        for campo in campos:
            empleado[campo] = input(f"ingrese {campo} del empleado")
            if campo == "Legajo":
                while validacion_int(empleado[campo]) is False:
                    print("debe ser un numero entero")
                    empleado[campo] = input(f"ingrese {campo} del empleado")

        lista.append(empleado)
        guardar = input("desea seguir agregando? si/no: " )    

    return lista

def crear_archivo(campos):
    archivo = input("ingrese nombre para el archivo  con extension .csv: ")

    try: 
        archivo_existe = os.path.isfile(archivo)
        if archivo_existe:
            print("Ese archivo ya existe")
            modif_archivo = input("Desea escribir o modificar el archivo?: \n 1. Modificar \n 2. Sobreescribir \n ")
            if modif_archivo == "1":
                modo_escritura = "a"
                encabezado = "no"
            
            if modif_archivo == "2":
                modo_escritura = "w"
                encabezado = "si"
        
        else:
            print("Se va a crear un archivo nuevo")

            modo_escritura = "w"
            encabezado = "si"
        print("hola2")

        with open(archivo, modo_escritura, newline='') as f:
            entrada_csv = csv.DictWriter(f, fieldnames=campos)
            print("hola")
            
            if encabezado == "si":
                entrada_csv.writeheader()
            lista = carga_datos(campos)
            entrada_csv.writerows(lista)
    
    

    except IOError:
        print("Hubo un error, no se puede visualizar el archivo") 



def consultar():
    
    try:
        archivo1 = input("ingrese nombre para el archivo de legajos con extension .csv: ")
        archivo2 = input("ingrese nombre para el archivo de viaticos con extension .csv: ")

        with open(archivo1, "r") as legajos, open(archivo2, "r") as viaticos:
            legajos_csv = csv.DictReader(legajos)
            viaticos_csv = csv.DictReader(viaticos)
            
            legajo_pedido = input("ingrese numero de legajo: ")
            while validacion_int(legajo_pedido) is False:
                    print("debe ser un numero entero")
                    legajo_pedido = input("ingrese numero de legajo: ")
            
        
            gasto = next(viaticos_csv, None) #adelantamos la 1er linea
            empleado = next(legajos_csv, None)
                    
            while empleado:
                while empleado and empleado["Legajo"] == legajo_pedido:
                    total = 0
                    while gasto:
                        while gasto and gasto["Legajo"] == legajo_pedido:
                            total += int(gasto["Gastos"])
                            gasto = next(viaticos_csv, None)

                        gasto = next(viaticos_csv, None)

                    diferencia = 5000 - total
                    if diferencia < 0:
                        print(f"Legajo {legajo_pedido}: {empleado['Nombre']},{empleado['Apellido']} gastó {total} y se ha pasado del presupuesto por {-(diferencia)}")
                    else:
                        print(f"Legajo {legajo_pedido}: {empleado['Nombre']},{empleado['Apellido']} gastó {total}")

                    empleado = next(legajos_csv, None)
                empleado = next(legajos_csv, None)    

    except IOError:
            print("Hubo un error, no se puede visualizar el archivo") 




def menu():
    CAMPOS = ["Legajo", "Apellido", "Nombre"]
    
    while True:
        print("-------------------------------")
        print("Gastos por viaticos")
        print("-------------------------------")
        print()
        print("Opciones disponibles:")
        print("1. Cargar datos")
        print("2. Calcular Viaticos")
        print("3. Salir")
        print()
        
        entrada_usuario = int(input("Seleccione una opcion: "))

        if entrada_usuario == 1:
            crear_archivo(CAMPOS)
        elif entrada_usuario == 2:
            consultar()
        elif entrada_usuario == 3:
            print("Fin del programa")
            exit()
                
        else:
            print('Error, solo de aceptan numeros del 1 al 3')


menu()