from database.client import DatabaseClient
from bson import json_util
import json
import customtkinter


def _init_database_client(db_uri: str, db_name: str) -> DatabaseClient:
    return DatabaseClient(db_uri=db_uri, db_name=db_name)


def database_restore(db_uri: str = "", db_name: str = "", db_file: str = "") -> None:
    modal = customtkinter.CTkToplevel()
    modal.title("Notification")
    modal.geometry("400x150")

    info_label = customtkinter.CTkLabel(master=modal)
    info_label.pack(pady=20, padx=20)

    close_button = customtkinter.CTkButton(
        master=modal, text="Acknowledge", command=modal.destroy)
    close_button.pack(pady=10, padx=20)

    if db_uri == "" or db_name == "" or db_file == "":
        info_label.configure(text="No db_uri provided")

    else:
        db_client = _init_database_client(db_uri=db_uri, db_name=db_name)

        print("DUMMY RESTORE WRAPPER")

        info_label.configure(
            text=f"Database {db_client.name()} \n saved to file database_backup.json")
