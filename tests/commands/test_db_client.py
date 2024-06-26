from unittest import mock
import mongomock
from pymongo import MongoClient
from pymongo.database import Database
from gridfs import Collection
from commands.db_client import DatabaseClient


db_uri = "DB_URI"
db_name = "DB_NAME"
db_client = DatabaseClient(db_uri, db_name)


# DATABASE MOCK PREPARATION ------------------------------
mock_collection = mongomock.MongoClient().db.collections
documents = [
    {
        "_id": 1,
        "user": "john",
        "description": "testing document",
    },
]
mock_collection.insert_many(documents)
# END OF DATABASE MOCK PREPARATION -----------------------


def _mock_collections(cls, *args, **kwargs) -> list[str]:
    return ["collection_one", "collection_two"]


def test_name() -> None:
    response = db_client.name()

    assert response == db_name


def test_collections() -> None:
     with mock.patch.object(DatabaseClient, 'collections', new=_mock_collections):
        response = db_client.collections()

        assert response == ["collection_one", "collection_two"]


def test_get_collection() -> None:
    response = db_client.get_collection(collection_name="collection_one")

    assert response == Collection(
        Database(
            MongoClient(
                host=["db_uri:27017"],
                document_class=dict,
                tz_aware=False,
                connect=True,
            ), 
            "DB_NAME"
        ), 
        "collection_one"
    )
