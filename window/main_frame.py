import customtkinter
from window import backup_view, restore_view


def main_frame(root_element: customtkinter.CTk) -> customtkinter.CTkFrame:
    frame = customtkinter.CTkFrame(master=root_element)
    frame.pack(pady=5, padx=5, fill="both", expand=True)

    tab_view = customtkinter.CTkTabview(master=frame)
    tab_view.pack(pady=20, padx=20, fill="both", expand=True)

    backup_view.backup_view(root_element=tab_view)
    restore_view.restore_view(root_element=tab_view)

    exit_button = customtkinter.CTkButton(master=frame,
                                          text="Exit",
                                          width=150,
                                          height=50,
                                          border_width=2,
                                          corner_radius=5,
                                          command=root_element.destroy)
    exit_button.pack(pady=50, padx=50)

    return frame
