from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
clientes = []

class Cliente:
    def __init__(self, nombre, correo, nit):
        self.nombre = nombre
        self.correo = correo
        self.nit = nit

@app.route('/')
def index():
    return render_template('index.html', clientes=clientes)

@app.route('/agregar_cliente', methods=['POST'])
def agregar_cliente():
    nombre = request.form['nombre']
    correo = request.form['correo']
    nit = request.form['nit']

    nuevo_cliente = Cliente(nombre, correo, nit)

    if any(cliente.nit == nit for cliente in clientes):
        return render_template('index.html', alerta=f"El cliente con NIT {nit} ya existe", clientes=clientes)

    clientes.append(nuevo_cliente)
    return render_template('index.html', exito="Cliente agregado exitosamente", clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True)