from controller.controller import valid

def main():
    nome = input('Digite seu nome: ')
    senha = input ('Digite sua senha: ')

    user_valid = valid(nome,senha)
    print(user_valid)
if __name__ == "__main__":
    main()
