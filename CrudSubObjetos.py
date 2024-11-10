import requests

BASE_URL = "http://localhost:5050"

# Función para ver todos los subobjetos de un objeto
def ver_subobjetos(token, obj_id):
    response = requests.get(
        f"{BASE_URL}/objetos/{obj_id}/subobjetos",
        headers={"Authorization": f"Bearer {token}"}
    )
    if response.status_code == 200:
        print("Subobjetos:", response.json())
    else:
        print("Error al obtener los subobjetos:", response.text)

# Función para ver un subobjeto por ID
def ver_subobjeto_por_id(token, obj_id, sub_id):
    response = requests.get(
        f"{BASE_URL}/objetos/{obj_id}/subobjetos/{sub_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    if response.status_code == 200:
        print("Subobjeto:", response.json())
    else:
        print("Error al obtener el subobjeto:", response.text)

# Función para añadir un subobjeto
def agregar_subobjeto(token, obj_id):
    subobjeto = {
        "subatributo": input("Introduce el subatributo: ")
    }
    response = requests.post(
        f"{BASE_URL}/objetos/{obj_id}/subobjetos",
        json=subobjeto,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    )
    if response.status_code == 201:
        print("Subobjeto añadido:", response.json())
    else:
        print("Error al añadir el subobjeto:", response.text)

# Función para modificar un subobjeto por ID
def modificar_subobjeto(token, obj_id, sub_id):
    modificaciones = {
        "subatributo": input("Introduce nuevo subatributo (deja vacío para no cambiar): ") or None
    }
    modificaciones = {k: v for k, v in modificaciones.items() if v is not None}
    response = requests.put(
        f"{BASE_URL}/objetos/{obj_id}/subobjetos/{sub_id}",
        json=modificaciones,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    )
    if response.status_code == 200:
        print("Subobjeto modificado:", response.json())
    else:
        print("Error al modificar el subobjeto:", response.text)

# Función para eliminar un subobjeto por ID
def eliminar_subobjeto(token, obj_id, sub_id):
    response = requests.delete(
        f"{BASE_URL}/objetos/{obj_id}/subobjetos/{sub_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    if response.status_code == 200:
        print(f"Subobjeto {sub_id} eliminado con éxito.")
    else:
        print("Error al eliminar el subobjeto:", response.text)
