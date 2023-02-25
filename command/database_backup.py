from database.client import DatabaseClient
from bson import json_util
import json


def _init_database_client(db_uri: str, db_name: str) -> DatabaseClient:
    return DatabaseClient(db_uri=db_uri, db_name=db_name)


def database_backup(db_uri: str = "", db_name: str = "") -> None:
    if db_uri == "" or db_name == "":
        print("No db_uri provided")
    else:
        db_client = _init_database_client(db_uri=db_uri, db_name=db_name)
        collections = db_client.collections()
        print(f"Connect to db: {db_client.name()}")

        with open("database_backup.json", "w", encoding="utf-8") as file:
            collection_dict: dict[str, list] = {}

            for collection in collections:
                entries = db_client.get_collection(collection).find()
                collection_dict[collection] = []

                while entries.alive:
                    collection_dict[collection].append(
                        json.loads(json_util.dumps(entries.next()))
                    )

            json.dump(collection_dict, file, ensure_ascii=False, indent=4)

        print(f"Db: {db_client.name()} saved to file")