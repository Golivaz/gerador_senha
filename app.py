from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

# Função para gerar senhas

def gerar_senha(tamanho, letras_min, letras_mai, numeros, especiais):

    caracteres = ''
    if letras_min:
        caracteres += string.ascii_lowercase
    if letras_mai:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if especiais:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

@app.route('/', methods=['GET', 'POST'])

def index():
    senha = None
    if request.method == 'POST':
        tamanho = int(request.form.get('tamanho', 12))  # Tamanho padrão: 12
        letras_min = 'letras_min' in request.form
        letras_mai = 'letras_mai' in request.form
        numeros = 'numeros' in request.form
        especiais = 'especiais' in request.form
        
        senha = gerar_senha(tamanho, letras_min, letras_mai, numeros, especiais)
    
    return render_template('index.html', senha=senha)

if __name__ == '__main__':
    app.run(debug=True, port=5001)