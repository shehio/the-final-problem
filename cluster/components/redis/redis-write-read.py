import redis

redis_host = '127.0.0.1' # Assuming port forwarding: kubectl port-forward --namespace default svc/my-redis-master 6379:6379
redis_port = 6379

# todo: Get the password from env variables
client = redis.Redis(host=redis_host, port=redis_port, password='') # fill in the password here

client.set('hello', 'world')

print(client.exists('hello'))

value = client.get('hello')
print(value.decode())
