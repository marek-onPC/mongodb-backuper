from database.client import DatabaseClient


def _init_database_client(db_uri: str, db_name: str) -> DatabaseClient:
    return DatabaseClient(db_uri=db_uri, db_name=db_name)


def database_connection(db_uri: str = "", db_name: str = "") -> None:
    if db_uri == "" or db_name == "":
        print("No db_uri provided")
    else:
        db_client = _init_database_client(db_uri=db_uri, db_name=db_name)
        collections = db_client.collections()
        print(f"Connect to db: {db_client.name()}")

        for collection in collections:
            print("Collection: " + collection)

            entries = db_client.get_collection(collection).find()

            while entries.alive:
                print(entries.next())
