from pymongo import MongoClient, database
from gridfs import Collection


class DatabaseClient:
    def __init__(self, db_uri: str, db_name: str) -> None:
        self.db_uri = db_uri
        self.db_name = db_name

    def connection(self) -> database.Database:
        client = MongoClient(self.db_uri, tls=True,
                             tlsAllowInvalidCertificates=True)
        database = client[self.db_name]
        return database

    def name(self) -> str:
        database = self.connection()
        name = database.name

        return name

    def collections(self) -> list[str]:
        database = self.connection()
        collections = database.list_collection_names()

        return collections


    def get_collection(self, collection_name: str) -> Collection:
        database = self.connection()
        collection = database[collection_name]

        return collection
