from commands.db_client import DatabaseClient
import customtkinter


def _init_database_client(db_uri: str, db_name: str) -> DatabaseClient:
    return DatabaseClient(db_uri=db_uri, db_name=db_name)


def database_restore(db_uri: str = "", db_name: str = "", db_file: str | None = None) -> None:
    modal = customtkinter.CTkToplevel()
    modal.title("Notification")
    modal.geometry("400x150")

    info_label = customtkinter.CTkLabel(master=modal)
    info_label.pack(pady=20, padx=20)

    close_button = customtkinter.CTkButton(
        master=modal, text="Acknowledge", command=modal.destroy)
    close_button.pack(pady=10, padx=20)

    if db_uri == "" or db_name == "" or db_file == None:
        info_label.configure(text="No db_uri provided")

    else:
        db_client = _init_database_client(db_uri=db_uri, db_name=db_name)

        for collection in db_file:
            for item in db_file[collection]:
                del item["_id"]

            db_client.get_collection(
                collection).insert_many(db_file[collection])

        info_label.configure(
            text=f"Database restored!")
