# ===========================================================
#   SISTEMA DE GESTIÓN DE TRANSPORTE URBANO – PROYECTO FINAL
# ===========================================================

from clases import Ruta, Bus, Conductor, Pasajero, Viaje
from datetime import datetime

TARIFA = 5000
CAPACIDAD_MAXIMA = 35
COSTO_FIJO = 6000  

# ===========================================================
#                  SISTEMA PRINCIPAL
# ===========================================================

class SistemaTransporte:
    def __init__(self):
        self.rutas = {}
        self.buses = {}
        self.conductores = {}
        self.pasajeros = {}
        self.viajes = {}

    # ------------------ REGISTROS ------------------ #

    def registrarRuta(self):
        print("\n--- Registrar Ruta ---")
        idRuta = int(input("ID Ruta: "))
        origen = input("Origen: ")
        destino = input("Destino: ")
        paradas = input("Paradas separadas por coma: ").split(",")
        horaSalida = input("Hora salida: ")
        horaLlegada = input("Hora llegada estimada: ")

        self.rutas[idRuta] = Ruta(idRuta, destino, origen, paradas, horaSalida, horaLlegada)
        print("✔ Ruta registrada.\n")

    def registrarBus(self):
        print("\n--- Registrar Bus ---")
        idBus = int(input("ID Bus: "))
        placa = input("Placa: ")

        bus = Bus(idBus, placa)
        self.buses[idBus] = bus
        print("✔ Bus registrado.\n")

    def registrarConductor(self):
        print("\n--- Registrar Conductor ---")
        idc = int(input("ID Conductor: "))
        nombre = input("Nombre: ")
        cedula = input("Cédula: ")
        telefono = input("Teléfono: ")

        self.conductores[idc] = Conductor(idc, nombre, cedula, telefono)
        print("✔ Conductor registrado.\n")

    def registrarPasajero(self):
        print("\n--- Registrar Pasajero ---")
        idp = int(input("ID Pasajero: "))
        saldo = int(input("Saldo tarjeta: "))
        ubicacion = input("Ubicación actual: ")

        self.pasajeros[idp] = Pasajero(idp, saldo, ubicacion)
        print("✔ Pasajero registrado.\n")

    # ------------------ OPERACIONES DE VIAJE ------------------ #

    def iniciarViaje(self):
        print("\n--- Iniciar Viaje ---")
        idViaje = int(input("ID del viaje: "))
        idRuta = int(input("ID de la ruta: "))
        idBus = int(input("ID del bus: "))
        idConductor = int(input("ID del conductor: "))

        if idRuta not in self.rutas or idBus not in self.buses or idConductor not in self.conductores:
            print("❌ Datos incorrectos.\n")
            return

        viaje = Viaje(idViaje, self.rutas[idRuta], self.buses[idBus], self.conductores[idConductor])
        self.viajes[idViaje] = viaje

        self.buses[idBus].viajeActivo = idViaje

        self.rutas[idRuta].asignarBus(self.buses[idBus])
        self.rutas[idRuta].asignarConductor(self.conductores[idConductor])

        print("✔ Viaje iniciado correctamente.\n")

    def registrarIngreso(self):
        print("\n--- Registrar Ingreso Pasajero ---")
        idPas = int(input("ID pasajero: "))
        idBus = int(input("ID bus: "))

        if idPas not in self.pasajeros:
            print("❌ Pasajero no existe.\n")
            return
        if idBus not in self.buses:
            print("❌ Bus no existe.\n")
            return

        pasajero = self.pasajeros[idPas]
        bus = self.buses[idBus]
        
        if bus.viajeActivo is None or bus.viajeActivo not in self.viajes:
            print("❌ El bus no tiene un viaje activo.\n")
            return
            
        viaje = self.viajes[bus.viajeActivo]

        if not pasajero.pagarPasaje():
            print("❌ Saldo insuficiente.\n")
            return

        if pasajero.registrarIngreso(bus):
            viaje.registrarPasajero()
            print("✔ Ingreso registrado.\n")
        else:
            print("❌ El bus está lleno.\n")

    def registrarSalida(self):
        print("\n--- Registrar Salida Pasajero ---")
        idPas = int(input("ID pasajero: "))
        idBus = int(input("ID bus: "))

        if idPas not in self.pasajeros:
            print("❌ Pasajero no existe.\n")
            return
        if idBus not in self.buses:
            print("❌ Bus no existe.\n")
            return

        pasajero = self.pasajeros[idPas]
        bus = self.buses[idBus]

        if pasajero.registrarSalida(bus):
            print("✔ Salida registrada.\n")
        else:
            print("❌ El pasajero NO está en el bus.\n")

    def consultarCuposBus(self):
        idBus = int(input("ID del bus: "))

        if idBus not in self.buses:
            print("❌ Bus no existe.\n")
            return

        bus = self.buses[idBus]
        cupos = bus.obtenerCupoDisponible()

        print(f"🚌 Cupos disponibles en el bus {idBus}: {cupos}\n")

    def consultarUbicacionBus(self):
        idBus = int(input("ID del bus: "))

        if idBus not in self.buses:
            print("❌ Bus no existe.\n")
            return

        bus = self.buses[idBus]
        print(f"🚌 Ubicación actual del bus {idBus}: {bus.ubicacionActual}\n")

    def cerrarViaje(self):
        idViaje = int(input("ID del viaje a cerrar: "))

        if idViaje not in self.viajes:
            print("❌ Ese viaje no existe.\n")
            return

        reporte = self.viajes[idViaje].cerrarViaje()
        
        bus_id = reporte["Bus"]
        if bus_id in self.buses:
            self.buses[bus_id].viajeActivo = None

        print("\n====== REPORTE DEL VIAJE ======")
        for k, v in reporte.items():
            print(f"{k}: {v}")
        print()


