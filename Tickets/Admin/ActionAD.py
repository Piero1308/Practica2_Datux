from Buses.Bus import *
from Conductores.Conductor import *

def showBus (lista_buses:list ):
    if len(lista_buses)>0:
        for i in lista_buses:
            print(i)
    else:
        print("No hay ningun bus, por favor agregue uno")

def AgregarBus (lista:list):
    IDBus=int(input("Ingrese el ID del bus: "))
    nombreCompany=input("Ingrese el nombre de la Compañia: ")
    tamaño=input("Ingrese el tamaño del bus (GRANDE) o (MEDIANO): ")
    marca=input("Ingrese la marca del bus: ")
    bus1=Busess(IDBus,nombreCompany,tamaño,marca)
    lista.append(bus1)

def showConductor (lista_conductor:list ):
    if len(lista_conductor)>0:
        for i in lista_conductor:
            print(i)
    else:
        print("No hay ningun conductor, por favor agregue uno")

def AgregarConductor (listaC:list):
    ID=int(input("Ingrese el ID del conductor: "))
    nombre=input("Ingrese el nombre del conductor: ")
    apellido=input("Ingrese el apellido del conductor: ")
    cond1=Conductor(ID,nombre,apellido)
    listaC.append(cond1)

def agregar_horario_conductor(conductor: list):
    if len(conductor) == 0:
        print("No hay conductores registrados, primero agrega uno.")
        return
    
    ID_conductor = int(input("Ingrese el ID del conductor al que desea asignar un horario: "))
    conductor_encontrado = None
    
    # Buscar el conductor por ID
    for conductor in conductor:
        if conductor.ID == ID_conductor:
            conductor_encontrado = conductor
            break
    
    if conductor_encontrado:
        horario = input("Ingrese el horario (ejemplo: Lunes 08:00-16:00): ")
        conductor_encontrado.agregar_horario(horario)
        print("Horario agregado correctamente.")
    else:
        print("No se encontró un conductor con ese ID.")

def agregar_ruta_bus(buses:list):
    if len(buses)==0:
        print("No hay rutas designadas, agrega una ruta. ")
        return
    rutaBus=int(input("Ingrese el ID del bus al que desea asignar una ruta: "))
    bus_encontrado=None
    # Buscar al bus por ID
    for buses in buses:
        if buses.IDBus == rutaBus:
            bus_encontrado = buses
            break

    if bus_encontrado:
        rutas= input("Designe una ruta(ejemplo: Lima-Callao): ")
        bus_encontrado.agregar_rutas(rutas)
        print("Ruta agregada correctamente")
    else:
        print("No se encontro un bus con ese ID. ")    
