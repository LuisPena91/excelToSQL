# Crear un diccionario con información de una persona
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "ocupacion": "Ingeniero"
}

# Iterar sobre el diccionario
for clave, valor in persona.items():
    print(f"{clave}: {valor}")