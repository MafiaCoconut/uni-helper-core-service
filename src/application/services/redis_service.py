from redis import Redis


class RedisService:
    def __init__(self,
                 redis_client: Redis
                 ):
        self.redis_client = redis_client

    def setex(self, key, value, time: int):
        return self.redis_client.setex(name=key, value=value, time=time)

    def ttl(self, key):
        return self.redis_client.ttl(name=key)
