from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal con menú
@app.route('/')
def index():
    return render_template("index.html")

# Ejercicio 1: formulario
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        precio_unitario = 9000
        total = tarros * precio_unitario

        # Descuentos según edad
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_descuento = total - (total * descuento)

        return render_template("resultado1.html",
                               nombre=nombre,
                               edad=edad,
                               total=total,
                               total_descuento=total_descuento,
                               descuento=descuento*100)
    return render_template("ejercicio1.html")

# Ejercicio 2: login
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario']
        clave = request.form['clave']

        # Usuarios predefinidos
        usuarios = {
            "juan": "admin",
            "pepe": "user"
        }

        if usuario in usuarios and clave == usuarios[usuario]:
            if usuario == "juan":
                mensaje = f"Bienvenido administrador {usuario}"
            else:
                mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template("resultado2.html", mensaje=mensaje)
    return render_template("ejercicio2.html")

if __name__ == '__main__':
    app.run(debug=True)
