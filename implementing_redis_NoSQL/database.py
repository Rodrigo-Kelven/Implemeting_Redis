from motor.motor_asyncio import AsyncIOMotorClient
import redis

# Configuração do MongoDB
MONGO_DETAILS = "mongodb://mongo:27017"
client = AsyncIOMotorClient(MONGO_DETAILS)
db = client.mydatabase
collection = db.mycollection

# Configuração do Redis
redis_client = redis.Redis(host='redis', port=6379, db=0)
