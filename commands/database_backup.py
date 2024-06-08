from commands.db_client import DatabaseClient
from bson import json_util
import json
import customtkinter


def _init_database_client(db_uri: str, db_name: str) -> DatabaseClient:
    return DatabaseClient(db_uri=db_uri, db_name=db_name)


def database_backup(db_uri: str = "", db_name: str = "") -> None:
    modal = customtkinter.CTkToplevel()
    modal.title("Notification")
    modal.geometry("400x150")

    info_label = customtkinter.CTkLabel(master=modal)
    info_label.pack(pady=20, padx=20)

    close_button = customtkinter.CTkButton(
        master=modal, text="Acknowledge", command=modal.destroy)
    close_button.pack(pady=10, padx=20)

    if db_uri == "" or db_name == "":
        info_label.configure(text="No db_uri provided")

    else:
        db_client = _init_database_client(db_uri=db_uri, db_name=db_name)
        collections = db_client.collections()

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

        info_label.configure(
            text=f"Database {db_client.name()} \n saved to file database_backup.json")
