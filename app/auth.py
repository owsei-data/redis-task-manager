from pymongo import MongoClient
import os
import bcrypt
import datetime

mongo_uri = os.getenv("MONGO_URI") #variavel local railway

#settings
client = MongoClient(mongo_uri)
db = client['task-manager'] #set db
colecao_user = db['user']

#registro
def registrar_user(login, senha):
    data_registro = datetime.datetime.now()
    try:

        senha_bytes = senha.encode('utf-8') #encodando pra bytes
        hash_senha = bcrypt.hashpw(senha_bytes, bcrypt.gensalt()) #encriptando a senha
        
        str_hash = hash_senha.decode('utf-8') #decodando

        r = colecao_user.insert_one({'login':login,'senha':str_hash}, data_criacao = data_registro) #setando no banco com senha criptada e decodada
        return True #retorno console
    except Exception as e:
        return False #retorno console


def verificar_senha(senha_fornecida, hash_armazenado):
    senha_bytes = senha_fornecida.encode('utf-8')
    hash_bytes = hash_armazenado.encode('utf-8')
    return bcrypt.checkpw(senha_bytes, hash_bytes) #check do bcrypt - retorna true se igual

'''
r = colecao_user.find_one({'login': 'edimilson'})
print(r)

r2 = verificar_senha('123batata','$2b$12$r1AwkZsp6bZKi.5vD2sjk.lyAU2iSoopq.ylZaFA7Rc17vms/jKYq')
print(r2)'''