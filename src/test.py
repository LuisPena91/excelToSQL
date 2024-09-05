persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
listVal = []

tupKey = tuple(persona.keys())
for i in range(len(tupKey)):
    listVal.append(persona[tupKey[i]])

tupleVal = f"({', '.join(listVal)})"

print(listVal)
print(tupleVal)