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

def agregar_horario_conductor(lista_conductores: list):
    if len(lista_conductores) == 0:
        print("No hay conductores registrados, primero agrega uno.")
        return
    
    ID_conductor = int(input("Ingrese el ID del conductor al que desea asignar un horario: "))
    conductor_encontrado = None
    
    # Buscar el conductor por ID
    for conductor in lista_conductores:
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

def Agregar_Horario_Bus(buses:list):
    if len(buses)==0:
        print("No hay horario asignado, agrega un horario. ")
        return
    horarioBus=int(input("Indique el ID del bus que desea asignar un horario: "))
    horario_encontrado=None
    # Buscar al bus por ID
    for buses in buses:
        if buses.IDBus==horarioBus:
            horario_encontrado=buses
            break
    if horario_encontrado:
        horarioB= input("Designe un horario: ")
        horario_encontrado.agregar_horario_bus(horarioB)
        print("Horario agregado correctamente")
    else:
        print("No se encontro un bus con ese ID. ")

def asignar_bus_conductor(lista_conductores: list, buses: list):

    ID_conductor = int(input("Ingrese el ID del conductor al que desea asignar un bus: "))
    conductor_encontrado = None

    # Buscar el conductor por ID
    for conductor in lista_conductores:
        if conductor.ID == ID_conductor:
            conductor_encontrado = conductor
            break

    if not conductor_encontrado:
        print("No se encontró un conductor con ese ID.")
        return

    ID_bus = int(input("Ingrese el ID del bus que desea asignar al conductor: "))
    bus_encontrado = None

    # Buscar el bus por ID
    for bus in buses:
        if bus.IDBus == ID_bus:
            bus_encontrado = bus
            break

    if not bus_encontrado:
        print("No se encontró un bus con ese ID.")
        return

    # Validar conflictos de horario
    for otro_conductor in lista_conductores:  
        if otro_conductor.bus_asignado == bus_encontrado.IDBus:
            for horario in conductor_encontrado.horarios:
                if horario in otro_conductor.horarios:  # Validación de horario
                    print(f"Conflicto de horario: El conductor {otro_conductor.nombre} ya tiene asignado el bus {bus_encontrado.IDBus} en el horario {horario}.")
                    return

    # Asignar el bus al conductor
    conductor_encontrado.bus_asignado = bus_encontrado.IDBus
    print(f"Bus {bus_encontrado.IDBus} asignado al conductor {conductor_encontrado.nombre} correctamente.")

    

