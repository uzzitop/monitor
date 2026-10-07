def contar_fuera(lecturas, minimo=8, maximo=14):
    conteo = {}
    for lectura in lecturas:
        t = lectura["temp_c"]
        m = lectura["maquina"]
        # PIEZA 1: si t está fuera de rango (menor que minimo o mayor que maximo)
        if t <minimo or t>maximo:
            conteo[m]=conteo.get(m,0)+1
        
    return conteo


datos = [
    {"maquina": "M01", "temp_c": 11.5},
    {"maquina": "M02", "temp_c": 15.2},
    {"maquina": "M03", "temp_c": 7.1},
    {"maquina": "M02", "temp_c": 16.0},
    {"maquina": "M01", "temp_c": 14.0},
    {"maquina": "M02", "temp_c": 20.0},
]
print(contar_fuera(datos))