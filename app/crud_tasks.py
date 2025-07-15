from pymongo import MongoClient
import os
import datetime as dt #pegar o horario de criacao das tasks
from bson.objectid import ObjectId #para convert do objectid dos registros task

mongo_uri = os.getenv('MONGO_URI')#env variable do railway
client = MongoClient(mongo_uri)

db = client('task-manager') #db atlas
colecao_tarefa = db['tarefas'] #tabela

#func crud para tarefas

#C - create
def criar_tarefa(titulo,descricao,deadline,status = 'Pendente'): #criar futuramente a conexao entre usuario e task
    data_criacao = dt.datetime.now().strftime('%d-%m-%y')
    tarefa ={ #dicionario
        'titulo' : titulo,
        'descricao' : descricao,
        'inicio' : data_criacao,
        'deadline' : deadline,
        'status' : status
    }
    registrar = colecao_tarefa.insert_one(tarefa) #registrando tarefa
    return str(registrar.inserted_id) #retornando id

#R - read
def ler_tarefa(id_tarefa):
    tarefa = colecao_tarefa.find_one({'_id': ObjectId(id_tarefa)}) #conversao
    if tarefa:
        return tarefa #retorna registro tarefa
    else:
        return None #none se n encontrado
#U - update



