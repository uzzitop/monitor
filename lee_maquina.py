import json

with open("maquina.json") as archivo:
    dato=json.load(archivo)

print(dato)
print(dato["maquina"])
print(dato["ubicacion"]["planta"])
print(sum(dato["lecturas"])/len(dato["lecturas"]))