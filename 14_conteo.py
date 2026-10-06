lecturas = [
    {"maquina": "M01", "errores": 0},
    {"maquina": "M02", "errores": 2},
    {"maquina": "M01", "errores": 1},
    {"maquina": "M03", "errores": 0},
    {"maquina": "M02", "errores": 3},
]
total = {}
for lectura in lecturas:
    m = lectura["maquina"]
    total[m] = total.get(m, 0) + lectura["errores"]
print(total)