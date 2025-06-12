from models.models import Createmessage
def valid(nome, senha):
   users = {
       "User" : "123",
       "User2" : "1234"
   }
   if nome in users and users[nome] == senha:
        return Createmessage.mensagem()
   else:
        return 'Usuário inválido'
