import redis
import uuid #para as hashs
import datetime as dt

r = redis.Redis(host = "localhost", port = 6379, db = 0, decode_responses = True) #conectando ao servidor local redis
r.set('teste', 'funciono')
print(r.get('teste'))

#funcoes crud
#C - create
def criar_tarefa(titulo,descricao,deadline,status='Pendente'): #func criar tarefa
    id_tarefa = str(uuid.uuid4()) #hash da tarefa
    chave = f'task:{id_tarefa}'
    
    data_inicio = dt.datetime.now().strftime("%d-%m-%y")#pegando data de criacao

    #salvar no redis
    r.hset(chave, mapping={
        'titulo': titulo,
        'descricao': descricao,
        'inicio': data_inicio,
        'deadline': deadline,
        'status': status
    })
    return id_tarefa #retorna o id criado

#R - read
def ler_tarefa(id_tarefa):
    chave = f'task:{id_tarefa}'
    if not r.exists(chave): #verficar existencia
        return None # nao achou task
    tarefa = r.hgetall(chave)
    return tarefa #retornar valores da task:id_tarefa

#U - update
def editar_tarefa(id_tarefa, **novos_campos): #func edit tarefa
    chave = f'task:{id_tarefa}'
    if not r.exists(chave):
        return None #nao existe

    r.hmset(chave, novos_campos) #atualizando com os dados
    return True
#D - delete
def deletar_tarefa(id_tarefa): #func del tarefa
    chave = f'task:{id_tarefa}'
    if not r.exists(chave):
        return None #nao existe
    r.delete(chave)
    return True
