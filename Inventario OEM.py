import json
import os

# Nombre del archivo donde se almacenarán las licencias
ARCHIVO_LICENCIAS = "licencias_oem.json"

def cargar_licencias():
    """Carga las licencias desde un archivo JSON, si existe."""
    if os.path.exists(ARCHIVO_LICENCIAS):
        with open(ARCHIVO_LICENCIAS, "r") as archivo:
            return json.load(archivo)
    return {}

def guardar_licencias(licencias):
    """Guarda las licencias en un archivo JSON."""
    with open(ARCHIVO_LICENCIAS, "w") as archivo:
        json.dump(licencias, archivo, indent=4)

def gestionar_licencias():
    licencias = cargar_licencias()

    while True:
        print("\nGestión de Licencias OEM")
        print("1. Agregar licencia")
        print("2. Mostrar todas las licencias")
        print("3. Eliminar una licencia")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            serial = input("Ingresa el número de serie de la laptop: ").strip()
            oem = input("Ingresa la licencia OEM: ").strip()
            
            if serial in licencias:
                print(f"La laptop con número de serie {serial} ya tiene una licencia registrada.")
            else:
                licencias[serial] = oem
                guardar_licencias(licencias)
                print(f"Licencia OEM registrada para el número de serie {serial}.")

        elif opcion == "2":
            if licencias:
                print("\nLicencias registradas:")
                for serial, oem in licencias.items():
                    print(f"Número de serie: {serial} | Licencia OEM: {oem}")
            else:
                print("No hay licencias registradas.")

        elif opcion == "3":
            serial = input("Ingresa el número de serie de la laptop que deseas eliminar: ").strip()
            if serial in licencias:
                del licencias[serial]
                guardar_licencias(licencias)
                print(f"Licencia asociada al número de serie {serial} eliminada.")
            else:
                print(f"No se encontró una licencia asociada al número de serie {serial}.")

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

# Llamada al programa principal
gestionar_licencias()