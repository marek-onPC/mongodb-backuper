import customtkinter
from command import database_backup, database_restore


def restore_view(root_element: customtkinter.CTkTabview) -> customtkinter.CTkFrame:
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

    db_file_input = customtkinter.CTkEntry(master=restore_view_wrapper,
                                           placeholder_text="DB JSON file",
                                           width=400,
                                           height=50,
                                           border_width=2,
                                           corner_radius=5)
    db_file_input.pack(pady=10, padx=20)

    restore_button = customtkinter.CTkButton(master=restore_view_wrapper,
                                             text="Prepare DB backup",
                                             width=150,
                                             height=50,
                                             border_width=2,
                                             corner_radius=5,
                                             command=lambda: database_restore.database_restore(db_uri_input.get(), db_name_input.get(), db_file_input.get()))
    restore_button.pack(pady=50, padx=50)

    return restore_view_wrapper
