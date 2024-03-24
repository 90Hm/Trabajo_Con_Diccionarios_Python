# En este código, se crea un diccionario llamado diccionario que contiene información sobre una persona
# llamada "Jhony Lex". Cada clave del diccionario interior representa un aspecto diferente de la información personal de "Jhony",
# como su edad, ciudad, profesión y número telefónico. La clave externa es el nombre de la persona y apunta al diccionario
# interno con su información personal.

# Para empezar, crearemos un diccionario con información personal ficticia

diccionario = {
    "Jhony Lex": {  # Clave: nombre de la persona
        "Edad": 25,  # Clave: edad
        "Ciudad": "Lago Agrio",  # Clave: ciudad
        "Profesion": "TIC",  # Clave: profesión (agregada)
        "Telefono": "0983546332"  # Clave: número telefónico (agregada)
    }
}
# Imprimimos el diccionario

print(diccionario)

# El resultado impreso seria algo asi:
# {'Jhony': {'Edad': 25, 'Ciudad': 'Lago Agrio', 'Profesion': 'TIC', 'Telefono': '0983546332'}}