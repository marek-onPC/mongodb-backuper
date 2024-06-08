import customtkinter
import json
from commands import database_restore


def _select_backup_file():
    global backup_db_file

    file = customtkinter.filedialog.askopenfile()
    backup_db_file = json.load(file)


def restore_view(root_element: customtkinter.CTkTabview) -> customtkinter.CTkFrame:
    global backup_db_file
    backup_db_file = None

    restore_view_wrapper = root_element.add("Restore")

    db_uri_input = customtkinter.CTkEntry(master=restore_view_wrapper,
                                          placeholder_text="MondoDB connection URL",
                                          width=400,
                                          height=50,
                                          border_width=2,
                                          corner_radius=5)
    db_uri_input.pack(pady=10, padx=20)

    db_name_input = customtkinter.CTkEntry(master=restore_view_wrapper,
                                           placeholder_text="Database name",
                                           width=400,
                                           height=50,
                                           border_width=2,
                                           corner_radius=5)
    db_name_input.pack(pady=10, padx=20)

    file_select_button = customtkinter.CTkButton(master=restore_view_wrapper,
                                                 text="Select file with DB backup",
                                                 width=150,
                                                 height=50,
                                                 border_width=2,
                                                 corner_radius=5,
                                                 command=lambda: _select_backup_file())
    file_select_button.pack(pady=25, padx=5)

    restore_button = customtkinter.CTkButton(master=restore_view_wrapper,
                                             text="Restore DB backup",
                                             width=150,
                                             height=50,
                                             border_width=2,
                                             corner_radius=5,
                                             command=lambda: database_restore.database_restore(db_uri_input.get(), db_name_input.get(), backup_db_file))
    restore_button.pack(pady=25, padx=5)

    return restore_view_wrapper
