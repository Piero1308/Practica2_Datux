class Busess:
    def __init__(self, IDBus, nombreCompany, tamaño, marca ):
        self.nombreCompany=nombreCompany
        self.IDBus=IDBus
        self.tamaño=tamaño
        self.marca=marca
        self.rutas=[]  #lista de rutas para cada bus
        self.horarioBus=[] #lista de horarios para cada bus
        
    def agregar_rutas(self, rutas):
        self.rutas.append(rutas)

    def agregar_horario_bus(self, horarioBus):
        self.horarioBus.append(horarioBus)    
        
    def __str__(self):
        return f"Bus ID: {self.IDBus}, nombre de la Compañia:{self.nombreCompany}, Tamaño: {self.tamaño}, Marca: {self.marca}, Ruta asignada: {self.rutas}, Horario Asignado:{self.horarioBus} "    
        
    #conductoresAsignado:Conductor[]
    #ruta
    #horarios=[]
    