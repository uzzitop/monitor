import os   
llave=os.environ.get("TICKETS_API_KEY")
if llave is None:
    print("Falta la variable TICKETS_API_KEY, Definila e intenta de nuevo.")
else:
    print(f"Llave encontrada:{len(llave)} caracteres")