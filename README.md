# Sistema de Gestión de Transporte Urbano

## Descripción

Sistema de gestión integral para transporte urbano desarrollado en Python que permite administrar rutas, buses, conductores y pasajeros de manera eficiente. El sistema facilita el control de operaciones en tiempo real, cálculo de ganancias y gestión de pagos mediante tarjetas virtuales.

## Objetivos

### Objetivo General
Desarrollar un programa informático que permita organizar de manera eficiente rutas, conductores y pasajeros de un sistema de transporte de buses, optimizando la toma de decisiones y perfeccionando el funcionamiento del servicio.

### Objetivos Específicos
- Estructurar módulo para organización de rutas y disponibilidad de buses
- Vincular conductores con rutas correspondientes automáticamente
- Mostrar registro de pasajeros en tiempo real con actualización máxima de 2 segundos
- Determinar ganancias generadas por cada viaje con cálculo preciso al 100%

## Características Principales

### Para Conductores
- Registro de pasajeros en tiempo real
- Visualización de total recaudado por ruta
- Control de inicio/fin de viaje
- Consulta de ruta asignada

### Para Pasajeros
- Consulta de ubicación de buses en tiempo real
- Verificación de cupos disponibles
- Recarga de tarjeta virtual
- Historial de viajes realizados

## Estructura del Proyecto

```
Proyecto_Transporte/
│
├── main/
│   └── sistemaTransporte.py          # Punto de entrada del programa
│
├── src/
│   ├── clases.py                     # Definición de clases principales
│   ├── sistemaPrincipal.py           # Lógica del sistema de transporte
│   └── menuPrincipal.py              # Interfaz de menú principal
│
├── docs/
│   ├── Proyecto_Programacion_de_Computadoresss.pdf  # Documentación del proyecto
│   ├── Pseudocodigo.pdf               # Pseudocódigo del sistema
│   ├── Diagrama_Flujo.pdf             # Diagrama de flujo del sistema
│   └── Presentacion_Diapositivas.pdf  # Diapositivas de presentación del proyecto
│
└── README.md                         # Este archivo
```

## ecnologías Utilizadas

- **Lenguaje:** Python 
- **Paradigma:** Programación Orientada a Objetos (POO)
- **Almacenamiento:** Estructuras de datos en memoria
- **Interfaz:** Consola de comandos


## Instrucciones de Ejecución

1. **Clonar o descargar** los archivos del proyecto manteniendo la estructura de carpetas

2. **Navegar** al directorio principal del proyecto:
   ```bash
   cd Proyecto_Transporte
   ```

3. **Ejecutar** el sistema desde el directorio principal:
   ```bash
   python main/sistemaTransporte.py
   ```

### Estructura de Archivos Correcta
Asegúrate de que los archivos estén organizados así:
```
Proyecto_Transporte/
├── main/
│   └── sistemaTransporte.py
├── src/
│   ├── clases.py
│   ├── sistemaPrincipal.py
│   └── menuPrincipal.py
└── docs/
    ├── Proyecto_Programacion_de_Computadoresss.pdf
    ├── Pseudocodigo.pdf
    ├── Diagrama_Flujo.pdf
    └── Presentacion_Diapositivas.pdf
```

## Uso del Sistema

### Menú Principal
El sistema presenta un menú con las siguientes opciones:

**Registros del Sistema:**
1. Registrar ruta
2. Registrar bus  
3. Registrar conductor
4. Registrar pasajero

**Operaciones:**
5. Iniciar viaje
6. Registrar ingreso pasajero
7. Registrar salida pasajero
8. Consultar cupos de un bus
9. Consultar ubicación de bus
10. Cerrar viaje
11. Salir

### Flujo de Trabajo Típico
1. Registrar rutas, buses, conductores y pasajeros
2. Iniciar un viaje asignando ruta, bus y conductor
3. Registrar ingresos y salidas de pasajeros
4. Consultar cupos y ubicaciones en tiempo real
5. Cerrar viaje para generar reporte de ganancias

## Reglas del Negocio

- Capacidad máxima por bus: 35 pasajeros
- Tarifa fija: $5.000 por trayecto
- Entre 3-6 paradas por ruta
- Máximo 7 rutas predefinidas
- Toda ruta debe tener conductor asignado
- Control de puestos mediante tarjeta de entrada/salida

## Autores

**Integrantes del Equipo:**
- Ivanna Castro Mendoza
- Daniela Silva Vargas  
- Tomás Rangel Palacio
- Nicolle Garaviz Sánchez

**Profesor:** Roy Alejandro Gómez Ávila

**Institución:** Universidad del Rosario - Facultad de Economía

**Curso:** Programación de Computadores

**Período:** 2025-II

## Notas del Proyecto

Este proyecto fue desarrollado como trabajo final del curso de Programación de Computadores, aplicando conceptos de Programación Orientada a Objetos, estructuras de datos y manejo de archivos en Python.

---

*Sistema desarrollado para optimizar la gestión del transporte urbano en ciudades como Bogotá* 
