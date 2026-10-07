# Reto: la máquina con más lecturas fuera de rango (8 a 14 °C).
# Hay lecturas sin dato: temp_c es None. No cuentan, pero hay que avisar cuántas fueron.

datos = [
    {"maquina": "M01", "temp_c": 11.5},
    {"maquina": "M02", "temp_c": 15.2},
    {"maquina": "M03", "temp_c": None},
    {"maquina": "M02", "temp_c": 16.0},
    {"maquina": "M01", "temp_c": 7.0},
    {"maquina": "M03", "temp_c": 7.5},
    {"maquina": "M03", "temp_c": None},
    {"maquina": "M03", "temp_c": 6.0},
    {"maquina": "M03", "temp_c": 5.0},
]

# PASO 1: una función que reciba datos y devuelva DOS cosas: el conteo y las ignoradas
def revisar(lecturas,minimo=8,maximo=14):
# PASO 2: dentro, recorre las lecturas; si temp_c es None, suma a ignoradas y sigue con la siguiente
    conteo={}
    ignoradas=0
    for lectura in lecturas:
        t=lectura["temp_c"]
        m=lectura["maquina"]
        if t==None:
            ignoradas+=1
            
        elif t<8 or t>14:
            conteo[m]=conteo.get(m,0)+1
            
    return conteo, ignoradas

conteo, ignoradas= revisar(datos)
mejor=max(conteo,key=conteo.get)

print(f"Las ignoradas son{ignoradas} y la maquina con mas lecturas es {mejor}")

            

# PASO 3: si no, y está fuera de rango, suma 1 al conteo de esa máquina
# PASO 4: fuera de la función, busca la máquina con el conteo mayor
# PASO 5: imprime "Ignoradas: N" y "Más fuera de rango: M03 (3)"
