import sqlite3
import pandas as pd


print("Conectando a la base de datos SQLite...")
# Conectar a la base de datos SQLite
conn = sqlite3.connect('shipment_database.db')
print("Conexión exitosa.")

# Leer y cargar Spreadsheet 0
print("Leyendo y cargando Spreadsheet 0...")
df_spreadsheet_0 = pd.read_csv('data/shipping_data_0.csv')
# Insertar datos en la base de datos
df_spreadsheet_0.to_sql('table_0', conn, index=False, if_exists='replace')
print("Spreadsheet 0 cargado exitosamente.")

# Realizar manipulaciones necesarias en df_spreadsheet_0
# ...


# Leer y cargar Spreadsheet 1
print("Leyendo y cargando Spreadsheet 1...")
df_spreadsheet_1 = pd.read_csv('data/shipping_data_1.csv')
# Insertar datos en la base de datos
df_spreadsheet_1.to_sql('table_1', conn, index=False, if_exists='replace')
print("Spreadsheet 1 cargado exitosamente.")

# Realizar manipulaciones necesarias en df_spreadsheet_1
# ...


# Leer y cargar Spreadsheet 2
print("Leyendo y cargando Spreadsheet 2...")
df_spreadsheet_2 = pd.read_csv('data/shipping_data_2.csv')
# Insertar datos en la base de datos
df_spreadsheet_2.to_sql('table_2', conn, index=False, if_exists='replace')
print("Spreadsheet 2 cargado exitosamente.")

# Realizar manipulaciones necesarias en df_spreadsheet_2
# ...


# Cerrar la conexión
conn.close()
print("Conexión cerrada.")
