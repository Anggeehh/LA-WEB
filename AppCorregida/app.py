import sqlite3
import os
from flask import Flask, render_template

app = Flask(__name__)

# Ruta absoluta a la base de datos (evita errores de "no encuentra el archivo")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "productos.db")

@app.route("/")
def ver_coleccion():
    conexion = sqlite3.connect(DB_PATH)
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()

    # Obtenemos los productos agrupados por categoría
    cursor.execute("SELECT * FROM productos WHERE categoria = 'drogueria' ORDER BY nombre")
    drogueria = cursor.fetchall()

    cursor.execute("SELECT * FROM productos WHERE categoria = 'fruteria' ORDER BY nombre")
    fruteria = cursor.fetchall()

    cursor.execute("SELECT * FROM productos WHERE categoria = 'bebidas' ORDER BY nombre")
    bebidas = cursor.fetchall()

    conexion.close()

    return render_template("indexgrupal.html",
                           drogueria=drogueria,
                           fruteria=fruteria,
                           bebidas=bebidas)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
