# Creamos el diccionario con la información personal ficticia
informacion_personal = {
    "nombre": "Juan",
    "edad": 23,
    "ciudad": "loja",
}

# Accedemos al valor de la clave "ciudad" y lo modificamos
informacion_personal["ciudad"] = "loja"

# Agregamos la clave "profesion" con su respectivo valor
informacion_personal["profesion"] = "chef"

# Verificamos si la clave "telefono" existe y la agregamos si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0982753208"

# Eliminamos la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimimos el diccionario final
print("Diccionario Final:")
print(informacion_personal)