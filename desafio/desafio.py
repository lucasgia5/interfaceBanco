#DESAFIO!!

#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental.
#  a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta

from flask import Flask, render_template, request

app = Flask(__name__)

contas = []
id_counter = 0  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/criar-conta', methods=['POST'])
def cria_conta():
    global id_counter
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')

    contas.append({"nome": nome, "cpf": cpf, "saldo": 0, "id": id_counter})
    id_counter += 1  

    return render_template('contaCriada.html', contas=contas, mensagem=None)

@app.route('/sacar/<int:conta_id>', methods=['POST'])
def sacar(conta_id):
    valor = float(request.form.get('valor'))
    for conta in contas:
        if conta['id'] == conta_id:
            if valor > conta['saldo']:
                mensagem = "Saldo insuficiente!"
                return render_template('contaCriada.html', contas=contas, mensagem=mensagem)
            else:
                conta['saldo'] -= valor
                mensagem = f"Seu saldo agora é de {conta['saldo']:.2f}"
                return render_template('contaCriada.html', contas=contas, mensagem=mensagem)
    return "Conta não encontrada!", 404

@app.route('/depositar/<int:conta_id>', methods=['POST'])
def depositar(conta_id):
    valor = float(request.form.get('valor'))
    for conta in contas:
        if conta['id'] == conta_id:
            conta['saldo'] += valor
            mensagem = f"Seu saldo agora é de {conta['saldo']:.2f}"
            return render_template('contaCriada.html', contas=contas, mensagem=mensagem)
    return "Conta não encontrada!", 404

if __name__ == '__main__':
    app.run(debug=True)
