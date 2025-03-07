from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Necesario para usar sesiones

# Contraseña para acceder (puedes cambiarla)
CONTRASENA = "Licenciada"

@app.route('/')
def inicio():
    if 'autenticado' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        contrasena = request.form['contrasena']
        if contrasena == CONTRASENA:
            session['autenticado'] = True
            return redirect(url_for('inicio'))
        else:
            flash('Contraseña incorrecta. Inténtalo de nuevo.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('autenticado', None)
    return redirect(url_for('login'))

@app.route('/trivia')
def trivia():
    return render_template('trivia.html')

@app.route('/memoria')
def memoria():
    return render_template('memoria.html')

@app.route('/rompecabezas')
def rompecabezas():
    return render_template('rompecabezas.html')

@app.route('/mensaje-final')
def mensaje_final():
    return render_template('mensaje-final.html')

if __name__ == '__main__':
    app.run(debug=True)