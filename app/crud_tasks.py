from pymongo import MongoClient
import os
import datetime #pegar o horario de criacao das tasks
from bson.objectid import ObjectId #para convert do objectid dos registros task
from bson.errors import InvalidId

mongo_uri = os.getenv('MONGO_URI')#env variable do railway
client = MongoClient(mongo_uri)

db = client['task-manager'] #db atlas
colecao_tarefa = db['tarefas'] #tabela

#func crud para tarefas

#C - create
def criar_tarefa(titulo,descricao,deadline,status = 'Pendente'): #criar futuramente a conexao entre usuario e task
    data_criacao = datetime.datetime.now() #datetime puro pro mongo
    tarefa ={ #dicionario
        'titulo' : titulo,
        'descricao' : descricao,
        'inicio' : data_criacao,
        'deadline' : deadline,
        'status' : status
    }
    r = colecao_tarefa.insert_one(tarefa) #registrando tarefa
    return str(r.inserted_id) #retornando id

#R - read
def ler_tarefa(id_tarefa):
    try:
        tarefa = colecao_tarefa.find_one({'_id': ObjectId(id_tarefa)}) #conversao
        if tarefa:
            return tarefa #retorna registro tarefa
        else:
            return None #none se n encontrado
    except InvalidId:
        print('id invalido')
        return None

#U - update
def atualizar_tarefa(id_tarefa, campo, novo_valor):
    try:
        filtro = {'_id': ObjectId(id_tarefa)} #filtro por id
        update = {'$set': {campo: novo_valor}} #update do valor da tarefa

        r = colecao_tarefa.update_one(filtro,update)
        if r.matched_count > 0: #verificando quantos docs foram modificados
            print(f"atualizada: {r.matched_count}")
            return True
        else:
            print("nao encontrada")
            return False
    except InvalidId:
        print('id invalido')
        return False

#D - delete
def deletar_tarefa(id_tarefa):

    try:
        filtro = {'_id': ObjectId(id_tarefa)} #filtro id
        
        r = colecao_tarefa.delete_one(filtro) #result

        if r.deleted_count > 0: #verificando quantos docs foram modificados
            print(f"deletada: {r.deleted_count}")
            return True
        else:
            print("nao encontrada")
            return False
    except InvalidId:
        print('id invalido')
        return None
'''
tarefa100 = criar_tarefa("aprender python", "quero aprender python", "10/12/2025")
r1 = colecao_tarefa.find_one({'titulo': 'aprender python'})
print(r1)

r2 = ler_tarefa("6876c0401a80747da3886dc9")

r2 = ler_tarefa("6876c0401a80747da3886dc9")
print(r2)

r3 = atualizar_tarefa("6876c0401a80747da3886dc9", "titulo", "aprender python 2x mais")
print(r3)
tarefinha = colecao_tarefa.find_one({'_id': ObjectId('6876c0401a80747da3886dc9')})
print(tarefinha)

r4 = deletar_tarefa("6876c0401a80747da3886dc9")
print(f'deletado: {r4}')'''