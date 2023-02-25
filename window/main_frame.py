import customtkinter
from command import database_connection


def main_frame(root_element: customtkinter.CTk) -> customtkinter.CTkFrame:
    frame = customtkinter.CTkFrame(master=root_element)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    db_uri_input = customtkinter.CTkEntry(master=frame,
                                          placeholder_text="MondoDB connection URL",
                                          width=400,
                                          height=50,
                                          border_width=2,
                                          corner_radius=5)
    db_uri_input.pack(pady=10, padx=20)

    db_name_input = customtkinter.CTkEntry(master=frame,
                                           placeholder_text="Database name",
                                           width=400,
                                           height=50,
                                           border_width=2,
                                           corner_radius=5)
    db_name_input.pack(pady=10, padx=20)

    button = customtkinter.CTkButton(master=frame,
                                     text="Connect to the DB",
                                     width=150,
                                     height=50,
                                     border_width=2,
                                     corner_radius=5,
                                     command=lambda: database_connection.database_connection(db_uri_input.get(), db_name_input.get()))
    button.pack(pady=50, padx=50)

    return frame
