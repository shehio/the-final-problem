import redis

# todo: Get the service ip from env variables
redis_host = ' ' # fill in the host here
redis_port = 6379

# todo: Get the password from env variables
client = redis.Redis(host=redis_host, port=redis_port, password=' ') # fill in the password here

client.set('hello', 'world')

print(client.exists('hello'))

value = client.get('hello')
print(value.decode())
