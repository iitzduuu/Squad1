from models import models

listaName = ['User' , 'User2']
listaSenha = ['123', '456']

def valid(nome, senha):
   if nome in listaName and senha in listaSenha:
        print(models.mensagem)
   else:
        print('Usuário inválido')