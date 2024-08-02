import redis
import os
from application.services.redis_service import RedisService

redis_client = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=os.getenv('REDIS_PORT', 6379), decode_responses=True)

redis_service = RedisService(
    redis_client=redis_client
)
