def maquina_con_mas_errores(lecturas):
    if len(lecturas) == 0:
        return None
    total = {}
    for lectura in lecturas:
        m = lectura["maquina"]
        total[m] = total.get(m, 0) + lectura["errores"]
    mejor = None
    for m in total:
        if mejor is None or total[m] > total[mejor]:
            mejor = m
    return mejor


datos = [
    {"maquina": "M01", "errores": 0},
    {"maquina": "M02", "errores": 2},
    {"maquina": "M01", "errores": 1},
    {"maquina": "M03", "errores": 0},
    {"maquina": "M02", "errores": 3},
]
print(maquina_con_mas_errores(datos))
print(maquina_con_mas_errores([]))
print(maquina_con_mas_errores([{"maquina": "M05", "errores": 0}]))