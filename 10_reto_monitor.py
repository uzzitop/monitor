maquina = input("Máquina (M01 a M05): ")
temp_c = float(input("Temperatura (°C): "))
errores = int(input("Errores del lector: "))

if temp_c < 8 or temp_c > 14:
    estado = "ALERTA: temperatura fuera de rango"
elif errores > 3:
    estado = "ALERTA: muchos errores del lector"
elif errores > 0:
    estado = "Revisar pronto"
else:
    estado = "Todo bien"

print(f"{maquina} -> {estado}")