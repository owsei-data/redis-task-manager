import pymongo as MongoClient
import os
import datetime

#mongo_uri = os.getenv("MONGO_URI")
#cliente = MongoClient("mongo_uri")
#db = cliente['task-manager']
#colecao_tarefa = db['tarefas']

def listar_tarefas(user_id): #listar todas as tarefas do usuario
    return list(colecao_tarefa.find({'user_id': user_id}))

def gerar_matriz_produtividade(tarefas, semanas=10): #matriz de produtividade
    hoje = datetime.date.today() #hoje
    matriz = [[0 for _ in range(7)] for _ in range(semanas)]
    for tarefa in tarefas:
        if tarefa['status'] == 'Concluída': #se a tarefa foi concluida
            data = tarefa['data_conclusao'].date() #data de conclusao
            delta = (hoje - data).days #delta entre hoje e data de conclusao
            semana = delta // 7 #semana
            dia = data.weekday() #dia da semana
            if 0 <= semana < semanas: #se a semana for menor que 10
                matriz[semanas - semana - 1][dia] += 1 #matriz[semana - 1][dia] += 1
    return matriz

#exemplo de uso matriz

tarefas_exemplo = [
    {'status': 'Concluída', 'data_conclusao': datetime.datetime(2024, 6, 24)},  #segunda
    {'status': 'Concluída', 'data_conclusao': datetime.datetime(2024, 6, 25)},  #terca
    {'status': 'Concluída', 'data_conclusao': datetime.datetime(2024, 6, 25)},  #terca
    {'status': 'Concluída', 'data_conclusao': datetime.datetime(2024, 6, 26)},  #quarta
    {'status': 'Concluída', 'data_conclusao': datetime.datetime(2024, 6, 27)},  #quinta
    {'status': 'Concluída', 'data_conclusao': datetime.datetime(2024, 6, 28)},  #sexta
    {'status': 'Concluída', 'data_conclusao': datetime.datetime(2024, 6, 29)},  #sabado
    {'status': 'Concluída', 'data_conclusao': datetime.datetime(2024, 6, 30)},  #domingo
    {'status': 'Concluída', 'data_conclusao': datetime.datetime(2024, 6, 24)},  #segunda
]

matriz = gerar_matriz_produtividade(tarefas_exemplo) #matriz de produtividade
print(matriz)