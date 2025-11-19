# ===========================================================
#   SISTEMA DE GESTIÓN DE TRANSPORTE URBANO – PROYECTO FINAL
# ===========================================================

from datetime import datetime

TARIFA = 5000
CAPACIDAD_MAXIMA = 35
COSTO_FIJO = 6000  # ✅ AGREGADO: Costo fijo por viaje


# ===========================================================
#                       CLASES PRINCIPALES
# ===========================================================

class Ruta:
    def __init__(self, idRuta, destino, origen, paradas, horaSalida, horaLlegada):
        self.idRuta = idRuta
        self.destino = destino
        self.origen = origen
        self.paradas = paradas
        self.horaSalida = horaSalida
        self.horaLlegadaEstimada = horaLlegada
        self.conductorAsignado = None
        self.busAsignado = None
        self.ubicacionActual = origen

    def asignarConductor(self, conductor):
        self.conductorAsignado = conductor
        conductor.asignarRuta(self.idRuta)

    def asignarBus(self, bus):
        self.busAsignado = bus
        bus.asignarRuta(self.idRuta)

    def actualizarUbicacion(self, nuevaUbicacion):
        self.ubicacionActual = nuevaUbicacion


class Bus:
    def __init__(self, idBus, placa):
        self.idBus = idBus
        self.placa = placa
        self.capacidad = CAPACIDAD_MAXIMA
        self.ubicacionActual = "Terminal"
        self.rutaAsignada = None
        self.pasajerosActuales = 0
        self.conductor = None
        self.viajeActivo = None  # ✅ AGREGADO: Para identificar el viaje activo

    def asignarRuta(self, ruta):
        self.rutaAsignada = ruta

    def asignarConductor(self, conductor):
        self.conductor = conductor

    def actualizarUbicacion(self, ubicacion):
        self.ubicacionActual = ubicacion

    def obtenerCupoDisponible(self):
        return self.capacidad - self.pasajerosActuales


class Conductor:
    def __init__(self, idConductor, nombre, cedula, telefono):
        self.idConductor = idConductor
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
        self.rutaActual = None
        self.totalGanancias = 0

    def asignarRuta(self, ruta):
        self.rutaActual = ruta

    def registrarGanancia(self, monto):
        self.totalGanancias += monto

    def obtenerGanancias(self):
        return self.totalGanancias


class Pasajero:
    def __init__(self, idPasajero, saldo, ubicacionActual):
        self.idPasajero = idPasajero
        self.saldoTarjeta = saldo
        self.ubicacionActual = ubicacionActual
        self.enBus = False

    def pagarPasaje(self):
        if self.saldoTarjeta >= TARIFA:
            self.saldoTarjeta -= TARIFA
            return True
        return False

    def registrarIngreso(self, bus):
        if bus.obtenerCupoDisponible() > 0:
            self.enBus = True
            bus.pasajerosActuales += 1
            return True
        return False

    def registrarSalida(self, bus):
        if self.enBus:
            self.enBus = False
            bus.pasajerosActuales -= 1
            return True
        return False

    def recargarTarjeta(self, monto):
        self.saldoTarjeta += monto


class Viaje:
    def __init__(self, idViaje, ruta, bus, conductor):
        self.idViaje = idViaje
        self.ruta = ruta
        self.bus = bus
        self.conductor = conductor
        self.pasajerosTransportados = 0
        self.gananciaGenerada = 0
        self.ingresosBrutos = 0  # ✅ AGREGADO: Para mostrar ingresos antes de costos
        self.costos = COSTO_FIJO  # ✅ AGREGADO: Costos fijos del viaje
        self.fecha = datetime.now().date()

    def registrarPasajero(self):
        self.pasajerosTransportados += 1

    def cerrarViaje(self):
        # ✅ MODIFICADO: Cálculo de ganancias considerando costos
        self.ingresosBrutos = self.pasajerosTransportados * TARIFA
        self.gananciaGenerada = self.ingresosBrutos - self.costos
        
        # Solo registrar ganancia si es positiva
        if self.gananciaGenerada > 0:
            self.conductor.registrarGanancia(self.gananciaGenerada)
        else:
            self.conductor.registrarGanancia(0)  # No ganancias negativas

        return {
            "Viaje": self.idViaje,
            "Ruta": self.ruta.idRuta,
            "Bus": self.bus.idBus,
            "Conductor": self.conductor.idConductor,
            "Pasajeros": self.pasajerosTransportados,
            "Tarifa por pasajero": f"${TARIFA:,}",
            "Ingresos brutos": f"${self.ingresosBrutos:,}",  # ✅ AGREGADO
            "Costos fijos": f"${self.costos:,}",  # ✅ AGREGADO
            "Ganancia neta": f"${self.gananciaGenerada:,}",  # ✅ MODIFICADO
            "Fecha": str(self.fecha)
        }

