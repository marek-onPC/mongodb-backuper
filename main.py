import customtkinter
from window import main_frame

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("640x480")

frame = main_frame.main_frame(root_element=app)

app.mainloop()
