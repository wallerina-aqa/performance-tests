from redis import Redis

cache = Redis(host="redis")
cache.set("example", 5)
print(int(cache.get("example")) ** 2)