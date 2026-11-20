
from flask import Flask, render_template, request

# Crear la aplicación Flask
app = Flask(__name__)


# Página principal
@app.route("/")
def inicio():
    return render_template("index.html")


# Ejercicio 1: cálculo de notas
@app.route("/notas", methods=["GET", "POST"])
def notas():

    resultado = None

    if request.method == "POST":

        nota1 = float(request.form["nota1"])
        nota2 = float(request.form["nota2"])
        nota3 = float(request.form["nota3"])
        asistencia = float(request.form["asistencia"])

        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= 40 and asistencia >= 75:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        resultado = {
            "promedio": round(promedio, 2),
            "asistencia": asistencia,
            "estado": estado
        }

    return render_template("notas.html", resultado=resultado)


# Ejercicio 2: comparación de nombres
@app.route("/nombres", methods=["GET", "POST"])
def nombres():

    resultado = None

    if request.method == "POST":

        nombre1 = request.form["nombre1"].strip()
        nombre2 = request.form["nombre2"].strip()
        nombre3 = request.form["nombre3"].strip()

        nombres = [nombre1, nombre2, nombre3]

        nombre_mayor = max(nombres, key=len)

        resultado = {
            "nombre": nombre_mayor,
            "cantidad": len(nombre_mayor)
        }

    return render_template("nombres.html", resultado=resultado)


# Iniciar el servidor
if __name__ == "__main__":
    app.run(debug=True)
