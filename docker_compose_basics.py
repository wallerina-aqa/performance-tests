from redis import Redis

cashe = Redis(host="redis")
cashe.incr("times")
print(cashe.get("times"))