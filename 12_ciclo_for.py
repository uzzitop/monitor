lecturas = [10.5, 11.2, 9.8, 14.7, 11.0]
fuera = 0
for temp in lecturas:
    if temp > 14:
        print(f"{temp} -> ALERTA")
        fuera = fuera + 1
    else:
        print(f"{temp} -> ok")
print(f"Lecturas fuera de rango: {fuera} de {len(lecturas)}")

menor=0
for temp in lecturas:
    if temp < 10:
        print(f"{temp} -> ALERTA")
        menor =+ 1
    else:
        print(f"{temp} -> ok")

print(f"Lecturas fuera de rango: {menor} de {len(lecturas)}")