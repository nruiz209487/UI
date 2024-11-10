import requests
from time import sleep
from CrudObjetos import *
from CrudSubObjetos import *

BASE_URL = "http://localhost:5050"

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\nOPCIONES:")
    print("1. Registrar nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Ver todos los objetos")
    print("4. Ver un objeto por ID")
    print("5. Añadir objeto")
    print("6. Modificar objeto")
    print("7. Eliminar objeto")
    print("8. Añadir Subobjeto.")
    print("9. Obtener Subobjetos por Objeto.")
    print("10. Obtener Subobjeto por ID.")
    print("11. Modificar Subobjeto.")
    print("12. Eliminar Subobjeto.")
    print("0. Salir")

# Función para registrar un nuevo usuario
def registrar_usuario():
    nombre = input("Escribe tu nombre de usuario: ")
    contrasenya = input("Escribe tu contraseña: ")
    response = requests.post(
        f"{BASE_URL}/usuarios/registrar",
        json={"nombre": nombre, "contrasenya": contrasenya},
        headers={"Content-Type": "application/json"}
    )
    print(response.text)

# Función para iniciar sesión y obtener un token
def iniciar_sesion():
    nombre = input("Usuario: ")
    contrasenya = input("Contraseña: ")
    response = requests.get(
        f"{BASE_URL}/usuarios/login",
        json={"nombre": nombre, "contrasenya": contrasenya},
        headers={"Content-Type": "application/json"}
    )
    if response.status_code == 200:
        token = response.json().get("token")
        print("Autenticación exitosa.")
        return token
    else:
        print("Error en la autenticación:", response.text)
        return None

# Bucle principal
def main():
    token = None
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            registrar_usuario()
        elif opcion == 2:
            token = iniciar_sesion()
        elif opcion == 3 and token:
            ver_objetos(token)
        elif opcion == 4 and token:
            ver_objeto_por_id(token)
        elif opcion == 5 and token:
            agregar_objeto(token)
        elif opcion == 6 and token:
            modificar_objeto(token)
        elif opcion == 7 and token:
            eliminar_objeto(token)
        elif opcion == 8:  # Añadir subobjeto
            obj_id = int(input("Introduce el ID del objeto: "))
            agregar_subobjeto(token, obj_id)
        elif opcion == 9:  # Obtener subobjetos por objeto
            obj_id = int(input("Introduce el ID del objeto: "))
            ver_subobjetos(token, obj_id)
        elif opcion == 10:  # Obtener subobjeto por ID
            obj_id = int(input("Introduce el ID del objeto: "))
            sub_id = int(input("Introduce el ID del subobjeto: "))
            ver_subobjeto_por_id(token, obj_id, sub_id)
        elif opcion == 11:  # Modificar subobjeto
            obj_id = int(input("Introduce el ID del objeto: "))
            sub_id = int(input("Introduce el ID del subobjeto a modificar: "))
            modificar_subobjeto(token, obj_id, sub_id)
        elif opcion == 12:  # Eliminar subobjeto
            obj_id = int(input("Introduce el ID del objeto: "))
            sub_id = int(input("Introduce el ID del subobjeto a eliminar: "))
            eliminar_subobjeto(token, obj_id, sub_id)
        elif opcion == 0:
            print("Ha salido del programa.")
            break
        else:
            print("Opción no válida o token no disponible.")

        sleep(2)

if __name__ == "__main__":
    main()
