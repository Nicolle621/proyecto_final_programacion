# ===========================================================
#                         MENÚ PRINCIPAL
# ===========================================================

def menu_principal(sistema):
    while True:
        print("""
=============== SISTEMA DE TRANSPORTE ===============

--- REGISTROS DEL SISTEMA ---
1. Registrar ruta
2. Registrar bus
3. Registrar conductor
4. Registrar pasajero

--- OPERACIONES ---
5. Iniciar viaje
6. Registrar ingreso pasajero
7. Registrar salida pasajero
8. Consultar cupos de un bus
9. Consultar ubicación de bus
10. Cerrar viaje

11. Salir
""")

        op = input("Seleccione una opción: ")

        if op == "1": sistema.registrarRuta()
        elif op == "2": sistema.registrarBus()
        elif op == "3": sistema.registrarConductor()
        elif op == "4": sistema.registrarPasajero()
        elif op == "5": sistema.iniciarViaje()
        elif op == "6": sistema.registrarIngreso()
        elif op == "7": sistema.registrarSalida()
        elif op == "8": sistema.consultarCuposBus()
        elif op == "9": sistema.consultarUbicacionBus()
        elif op == "10": sistema.cerrarViaje()
        elif op == "11":
            print("Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida.\n")


