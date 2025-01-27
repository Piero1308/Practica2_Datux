# Realice un programa que pueda gestionar tickets de buses
# las clases a usar seran buses  , conductores
# 1. Un menu iteractivo con las siguiente opciones: agregar bus , agregar ruta a bus 
# registrar horario a bus, agregar conductor , agregar horario a conductor(*) y asignar bus a conductor(**)
# * consideremos que el horario de los conductores solo es a nivel de horas mas no dias ni fechas
# **validar que no haya conductores en ese horario ya asignados
class Conductor:
    def __init__(self, ID, nombre, apellido ):
        self.ID=ID
        self.nombre=nombre
        self.apellido=apellido
        self.horarios = []  # Lista para almacenar horarios

    def agregar_horario(self, horario):
        self.horarios.append(horario)
    def __str__(self):
        return f"ID del Conductor: {self.ID}, Nombre: {self.nombre}, Apellido: {self.apellido}, horario:{self.horarios}"
        
    
    




