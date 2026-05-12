import sqlite3
import os

# Ruta absoluta a la base de datos (mismo sitio que este archivo)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "productos.db")

def inicializar_base_de_datos():
    print(f"Conectando a la BD en: {DB_PATH}")
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    # -------------------------------------------------------
    # 1. BORRAR la tabla si ya existe (para empezar desde cero)
    # -------------------------------------------------------
    cursor.execute("DROP TABLE IF EXISTS productos")
    print("Tabla antigua eliminada (si existía).")

    # -------------------------------------------------------
    # 2. CREAR la tabla con todas las columnas necesarias
    # -------------------------------------------------------
    cursor.execute("""
        CREATE TABLE productos (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre           TEXT    NOT NULL,
            fecha_caducidad  TEXT,
            categoria        TEXT,
            marca            TEXT,
            precio           TEXT,
            stock            TEXT,
            imagen           TEXT
        )
    """)
    print("Tabla 'productos' creada.")

    # -------------------------------------------------------
    # 3. INSERTAR los productos iniciales
    #    Formato de cada fila:
    #    (nombre, fecha_caducidad, categoria, marca, precio, stock, imagen)
    #
    #    - categoria debe ser: 'drogueria', 'fruteria' o 'bebidas'
    #    - imagen debe coincidir con un archivo en static/img/
    # -------------------------------------------------------
    productos = [
        # --- DROGUERÍA ---
        ("Lejía", "2027-06-30", "drogueria", "Neutrex", "1.50€", "50", "lejia.png"),
        ("Detergente",     "2027-12-01", "drogueria", "Marsella",  "3.99€", "245", "detergente.png"),
        ("Oxígeno Activo", "2026-09-15", "drogueria", "Ace",       "4.50€", "100", "oxigeno.png"),
        ("Limpiacristales", "2027-08-19", "drogueria", "3 brujas",       "2.50€", "10", "oxigeno.png"),


        # --- FRUTERÍA ---
        ("Manzana",        "2026-05-10", "fruteria",  "Frutas del Campo",   "2.99€", "54", "manzana-removebg-preview.png"),
        ("Albaricoque",    "2026-05-05", "fruteria",  "Frutas del Sur",     "3.50€", "20", "albaricoque.png"),
        ("Pera",           "2026-05-08", "fruteria",  "Frutas Selectas",    "2.75€", "67", "peras.png"),

        # --- BEBIDAS ---
        ("Agua",           "2080-03-07", "bebidas",   "Solán de Cabras",    "0.99€", "200", "agua.png"),
        ("Coca Cola",      "2027-01-15", "bebidas",   "Coca-Cola",          "1.50€", "300", "coca.png"),
        ("Nestea",         "2026-11-20", "bebidas",   "Nestlé",             "1.20€", "190", "nestea.png"),
    ]

    cursor.executemany("""
        INSERT INTO productos (nombre, fecha_caducidad, categoria, marca, precio, stock, imagen)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, productos)

    conexion.commit()
    print(f"{len(productos)} productos insertados correctamente.")

    # -------------------------------------------------------
    # 4. VERIFICAR que todo se guardó bien
    # -------------------------------------------------------
    cursor.execute("SELECT id, nombre, categoria FROM productos ORDER BY categoria, nombre")
    filas = cursor.fetchall()
    print("\n--- Productos en la BD ---")
    for fila in filas:
        print(f"  [{fila[0]}] {fila[2]:<12} → {fila[1]}")

    conexion.close()
    print("\n Base de datos lista.")

# Ejecutar solo si se llama directamente (no si se importa)
if __name__ == "__main__":
    inicializar_base_de_datos()
