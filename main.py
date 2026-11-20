
from flask import Flask, render_template, request, redirect, url_for, abort

# Crear la aplicación Flask
app = Flask(__name__)


# ==========================================
# MENÚ PRINCIPAL
# ==========================================

@app.route("/")
def inicio():
    return render_template("index.html")


# ==========================================
# RUTAS CON PARÁMETROS Y REDIRECCIONES
# ==========================================

@app.route("/ejercicio/<int:numero>")
def seleccionar_ejercicio(numero):

    # Si el número es 1, ir al cálculo de notas
    if numero == 1:
        return redirect(url_for("notas"))

    # Si el número es 2, ir a la comparación de nombres
    elif numero == 2:
        return redirect(url_for("nombres"))

    # Si el ejercicio no existe, mostrar error 404
    else:
        abort(404)


# ==========================================
# EJERCICIO 1: CÁLCULO DE NOTAS
# ==========================================

@app.route("/notas", methods=["GET", "POST"])
def notas():

    resultado = None

    if request.method == "POST":

        # Recibir los datos del formulario
        nota1 = float(request.form["nota1"])
        nota2 = float(request.form["nota2"])
        nota3 = float(request.form["nota3"])
        asistencia = float(request.form["asistencia"])

        # Calcular el promedio de las tres notas
        promedio = (nota1 + nota2 + nota3) / 3

        # Comprobar las condiciones de aprobación
        if promedio >= 40 and asistencia >= 75:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        # Guardar los resultados en un diccionario
        resultado = {
            "promedio": round(promedio, 2),
            "asistencia": asistencia,
            "estado": estado
        }

    # Mostrar la plantilla con el resultado
    return render_template("notas.html", resultado=resultado)


# ==========================================
# EJERCICIO 2: COMPARACIÓN DE NOMBRES
# ==========================================

@app.route("/nombres", methods=["GET", "POST"])
def nombres():

    resultado = None

    if request.method == "POST":

        # Recibir los tres nombres ingresados
        nombre1 = request.form["nombre1"].strip()
        nombre2 = request.form["nombre2"].strip()
        nombre3 = request.form["nombre3"].strip()

        # Almacenar los nombres en una lista
        nombres = [nombre1, nombre2, nombre3]

        # Identificar el nombre con mayor cantidad de caracteres
        nombre_mayor = max(nombres, key=len)

        # Guardar el resultado en un diccionario
        resultado = {
            "nombre": nombre_mayor,
            "cantidad": len(nombre_mayor)
        }

    # Mostrar la plantilla con el resultado
    return render_template("nombres.html", resultado=resultado)


# ==========================================
# INICIAR EL SERVIDOR
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)
