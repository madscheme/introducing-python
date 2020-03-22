import redis

conn = redis.Redis()
print('Dryer is starting')
while True:
    msg = conn.blpop('dishes')
    if not msg:
       break
    val = msg[1].decode('utf-8')
    if val == 'quit':
       break
    print('Dried', val)
print('Dishes are dried')
