import redis

redis_host = 'my-redis-master'
redis_port = 6379

client = redis.Redis(host=redis_host, port=redis_port, password='hello-world')

client.set('key', 'value')
client.setex('key_expiring', 10, 'value_expiring')

value = client.get('key')
print(value.decode())

print(client.exists('key'))