from motor.motor_asyncio import AsyncIOMotorClient
from store.core.config import settings


class MongoClient:
    def __init__(self) -> None:
        self.client = AsyncIOMotorClient(settings.DATABASE_URL)

    def get(self) -> AsyncIOMotorClient:
        return self.client


db_client = MongoClient()
