#Importar la biblioteca de flask
from flask import Flask, redirect, render_template, request, url_for, flash


#Objeto para inicilizar la aplicacion
#1. nombre por defecto
#2. ruta donde esta los templates o nombre de la carpeta
app = Flask(__name__, template_folder='plantillas')

#Clave secreta de la aplicacion
app.secret_key = '123456789'


#Arreglo para almacenar las tareas
lista_tareas = []

#Controlador de la ruta por defecto
# Ingreso de datos por formulario
# Mostras las tareas pendientes
@app.route('/')
def principal():
    return render_template('principal.html', lista_tareas=lista_tareas)


#Controlador para enviar los datos
@app.route('/enviar', methods=['POST'])
def enviar():
    if request.method == 'POST':

        tarea_descripcion = request.form['tarea_descripcion']
        tarea_correo = request.form['tarea_correo']
        tarea_prioridad = request.form['tarea_prioridad']


        if tarea_descripcion == '' or tarea_correo == '':
            flash('Por favor ingresar todos los campos de texto  y verificar que no esten vacios')
            return redirect(url_for('principal'))
        else:

            flash('Se agrego una nueva tarea a la lista')

            lista_tareas.append({'tarea_descripcion': tarea_descripcion, 'tarea_correo': tarea_correo, 'tarea_prioridad': tarea_prioridad })

            return redirect(url_for('principal'))

#Controlador de la ruta para borrar
@app.route('/borrar', methods=['POST'])
def borrar():
    if request.method == 'POST':
        
        if lista_tareas == []:

            flash('No existen tareas en la lista')
            return redirect(url_for('principal'))

        else:
            lista_tareas.clear()
            flash('La lista de tareas fue borrada')
            return redirect(url_for('principal'))


#Metodo para correr la aplicacion
if __name__ == '__main__':
    app.run(debug=True)