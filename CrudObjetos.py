import requests
BASE_URL = "http://localhost:5050"
# Función para ver todos los objetos
def ver_objetos(token):
    response = requests.get(
        f"{BASE_URL}/objetos",
        headers={"Authorization": f"Bearer {token}"}
    )
    if response.status_code == 200:
        print("Objetos:", response.json())
    else:
        print("Error al obtener los objetos:", response.text)

# Función para ver un objeto por ID
def ver_objeto_por_id(token):
    obj_id = int(input("Introduce el ID del objeto: "))
    response = requests.get(
        f"{BASE_URL}/objetos/{obj_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    if response.status_code == 200:
        print("Objeto:", response.json())
    else:
        print("Error al obtener el objeto:", response.text)

# Función para añadir un objeto
def agregar_objeto(token):
    nuevo_objeto = {
        "atributo1": input("Introduce atributo1: "),
        "atributo2": int(input("Introduce atributo2 (número): ")),
        "atributo3": input("Introduce atributo3 (True/False): ").strip().lower() == "true",
        "atributo5": input("Introduce atributo5: ")
    }
    response = requests.post(
        f"{BASE_URL}/objetos",
        json=nuevo_objeto,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    )
    if response.status_code == 201:
        print("Objeto añadido:", response.json())
    else:
        print("Error al añadir el objeto:", response.text)

# Función para modificar un objeto por ID
def modificar_objeto(token):
    obj_id = int(input("Introduce el ID del objeto a modificar: "))
    modificaciones = {
        "atributo1": input("Introduce nuevo atributo1 (deja vacío para no cambiar): ") or None,
        "atributo2": input("Introduce nuevo atributo2 (deja vacío para no cambiar): ") or None,
        "atributo3": input("Introduce nuevo atributo3 (True/False, deja vacío para no cambiar): ").strip().lower() or None,
        "atributo5": input("Introduce nuevo atributo5 (deja vacío para no cambiar): ") or None
    }
    modificaciones = {k: v for k, v in modificaciones.items() if v is not None}
    response = requests.put(
        f"{BASE_URL}/objetos/{obj_id}",
        json=modificaciones,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    )
    if response.status_code == 200:
        print("Objeto modificado:", response.json())
    else:
        print("Error al modificar el objeto:", response.text)

# Función para eliminar un objeto por ID
def eliminar_objeto(token):
    obj_id = int(input("Introduce el ID del objeto a eliminar: "))
    response = requests.delete(
        f"{BASE_URL}/objetos/{obj_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    if response.status_code == 200:
        print(f"Objeto {obj_id} eliminado con éxito.")
    else:
        print("Error al eliminar el objeto:", response.text)
