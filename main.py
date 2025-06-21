from controller.controller import valid

def main():
    nome = input('Digite seu nome: ')
    senha = input ('Digite sua senha: ')

    user_valid = valid(nome,senha)
    print(user_valid)
if __name__ == "__main__":
    main()

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    nome = data.get('nome')
    senha = data.get('senha')

    if nome in users and users[nome] == senha:
        return jsonify({'mensagem': 'Login válido!'})
    else:
        return jsonify({'mensagem': 'Usuário inválido'})