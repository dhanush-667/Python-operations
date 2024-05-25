import os
import random
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0
    
    message = ""
    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['attempts'] += 1
        
        if guess < session['number']:
            message = "Too low! Try again."
        elif guess > session['number']:
            message = "Too high! Try again."
        else:
            message = f"Congratulations! You guessed the number {session['number']} in {session['attempts']} attempts."
            session.pop('number')
            session.pop('attempts')
    
    return render_template('index.html', message=message)

@app.route('/restart')
def restart():
    session.pop('number', None)
    session.pop('attempts', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

