import redis
import uuid #para as hashs

r = redis.Redis(host = "localhost", port = 6379, db = 0, decode_responses = True) #conectando ao servidor local redis
r.set('teste', 'funciono')
print(r.get('teste'))