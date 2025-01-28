# Realice un programa que pueda gestionar tickets de buses
# las clases a usar seran buses  , conductores
# 1. Un menu iteractivo con las siguiente opciones: agregar bus , agregar ruta a bus 
# registrar horario a bus, agregar conductor , agregar horario a conductor(*) y asignar bus a conductor(**)
# * consideremos que el horario de los conductores solo es a nivel de horas mas no dias ni fechas
# **validar que no haya conductores en ese horario ya asignados
from Admin.ActionAD import *
from Buses.Bus import *
from Conductores.Conductor import *
def Menu():
    msg="""
BIENVENIDO
GESTIONE SU TICKET DE BUS
1)VER BUSES DISPONIBLES
2)AGREGAR BUS
3)AGREGAR RUTA A BUS
4)VER CONDUCTOR DISPONIBLE
5)AGREGAR CONDUCTOR
6)AGREGAR HORARIO A CONDUCTOR
7)REGISTRAR HORARIO A BUS
8)ASIGNAR BUS A CONDUCTOR
9)SALIR
""" 
    
    lista_conductores=[]
    buses=[]
    while True:
        print(msg)
        option=int(input("Ingrese una opcion del Menu: "))
        match option:
            case 1:
                showBus(buses)
            case 2:
                AgregarBus(buses)
            case 3:
                agregar_ruta_bus(buses)
            case 4:
                showConductor(lista_conductores)
            case 5:
                AgregarConductor(lista_conductores)
            case 6:
                agregar_horario_conductor(lista_conductores)
            case 7:
                Agregar_Horario_Bus(buses)
            case 8:
                asignar_bus_conductor(lista_conductores,buses)
            case 9:
                print("VUELVA PRONTO")
                break
            case _:
                print("INGRESE UNA OPCION VALIDA")

