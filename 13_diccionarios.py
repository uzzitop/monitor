lectura = {"maquina": "M02", "temp_c": 11.5, "errores": 1}
print(lectura["maquina"])
print(lectura["temp_c"])
lectura["errores"] = 3
lectura["estado"] = "revisar"
print(lectura)
print(lectura.get("humedad", "sin dato"))
for clave, valor in lectura.items():
    print(clave, "=", valor)