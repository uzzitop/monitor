# Vending machine monitor (Python + SQLite)

Practice project: a simulator creates sensor readings for 5 vending machines, Python scripts read and check them, and SQL answers questions about them.

## Flow

`simulador.py` → `lecturas.csv` → `cargar_datos.py` → `monitor.db` (SQLite) → `consulta1-5.sql` via `correr_sql.py`

## Main files

| File | What it does |
|---|---|
| `simulador.py` | Creates a week of readings (temperature, reader errors) for machines M01 to M05, then keeps adding live readings. |
| `cargar_datos.py` | Loads `lecturas.csv` into a SQLite table. |
| `consulta1.sql` … `consulta5.sql` | Questions in SQL (counts, GROUP BY, filters). |
| `correr_sql.py` | Runs a `.sql` file against `monitor.db` and prints the result. |
| `lee_maquina.py`, `maquina.json` | Reads a machine's nested JSON (location, readings) and averages its readings. `esquema.json` is its JSON Schema. |
| `usar_llave.py` | Reads an API key from an environment variable (`.env`), never from the code. |
| `10_…` to `22_…` | Python exercises: lists, loops, dictionaries, functions, CSV, JSON and error handling. |

## How to run it

```
python simulador.py      # Ctrl + C after a few seconds
python cargar_datos.py
python correr_sql.py consulta1.sql
```

Only the Python standard library is needed. `lecturas.csv` and `monitor.db` are generated, so they are not in the repo.
