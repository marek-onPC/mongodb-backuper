import customtkinter
from commands import database_backup


def backup_view(root_element: customtkinter.CTkTabview) -> customtkinter.CTkFrame:
    backup_view_wrapper = root_element.add("Backup")

    db_uri_input = customtkinter.CTkEntry(master=backup_view_wrapper,
                                          placeholder_text="MondoDB connection URL",
                                          width=400,
                                          height=50,
                                          border_width=2,
                                          corner_radius=5)
    db_uri_input.pack(pady=10, padx=20)

    db_name_input = customtkinter.CTkEntry(master=backup_view_wrapper,
                                           placeholder_text="Database name",
                                           width=400,
                                           height=50,
                                           border_width=2,
                                           corner_radius=5)
    db_name_input.pack(pady=10, padx=20)

    backup_button = customtkinter.CTkButton(master=backup_view_wrapper,
                                            text="Prepare DB backup",
                                            width=150,
                                            height=50,
                                            border_width=2,
                                            corner_radius=5,
                                            command=lambda: database_backup.database_backup(db_uri_input.get(), db_name_input.get()))
    backup_button.pack(pady=50, padx=50)

    return backup_view_wrapper
