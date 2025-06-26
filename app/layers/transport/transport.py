# capa de transporte/comunicación con otras interfaces o sistemas externos.

import requests
from ...config import config

# comunicación con la REST API.
# este método se encarga de "pegarle" a la API y traer una lista de objetos JSON.
def getAllImages():
    json_collection = []
    for id in range(1, 20): # se itera desde 1 hasta 20 (exclusivo) para obtener los Pokémon con esos ID.
        response = requests.get(config.STUDENTS_REST_API_URL + str(id)) # se realiza una solicitud GET a la API para obtener los datos del Pokémon con el ID actual.

        # si la búsqueda no arroja resultados, entonces retornamos una lista vacía de elementos.    
        if not response.ok:
            print(f"[transport.py]: error al obtener datos para el id {id}") # se imprime un mensaje de error si la solicitud no fue exitosa.
            continue

        raw_data = response.json() # se convierte la respuesta en formato JSON.

        if 'detail' in raw_data and raw_data['detail'] == 'Not found.': # si el JSON contiene un campo 'detail' con el valor 'Not found.', significa que no se encontró el Pokémon con ese ID.
            print(f"[transport.py]: Pokémon con id {id} no encontrado.")
            continue

        json_collection.append(raw_data) # se agrega el objeto JSON del Pokémon a la lista json_collection.

    return json_collection #retorna la lista de objetos JSON que representan los Pokémon obtenidos de la API.

# obtiene la imagen correspodiente para un type_id especifico 
def get_type_icon_url_by_id(type_id):
    base_url = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/colosseum/'
    return f"{base_url}{type_id}.png"