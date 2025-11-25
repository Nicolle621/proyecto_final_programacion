# ===========================================================
#   SISTEMA DE GESTIÓN DE TRANSPORTE URBANO – PROYECTO FINAL
# ===========================================================
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)  # Directorio Proyecto Progra
src_path = os.path.join(parent_dir, 'src')
sys.path.append(src_path)


from menuPrincipal import menu_principal
from clases import Ruta, Bus, Conductor, Pasajero, Viaje
from sistemaPrincipal import SistemaTransporte


from menuPrincipal import menu_principal
from sistemaPrincipal import SistemaTransporte


# ===========================================================
#                     INICIO DEL PROGRAMA
# ===========================================================

if __name__ == "__main__":
    sistema = SistemaTransporte()
    menu_principal(sistema)