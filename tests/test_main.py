from typing import cast
import pytest
from unittest.mock import MagicMock
import customtkinter
from gui import main_frame


@pytest.fixture
def mock_app():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    
    app = customtkinter.CTk()
    app.title("MongoDB backuper")
    app.geometry("800x640")
    
    frame = main_frame.main_frame(root_element=app)
    yield app, frame
    
    app.destroy()


def test_main_tabs(mock_app):
    app, frame = mock_app

    tab = frame.winfo_children()[0]
    button = frame.winfo_children()[1]

    tab = cast(customtkinter.CTkTabview, tab)
    button = cast(customtkinter.CTkButton, button)

    # Assert current view
    assert tab.get() == "Backup"

    # Select and assert 'Restore' view
    tab.set("Restore")
    assert tab.get() == "Restore"

    # Assert exit button
    assert button.cget("text") == "Exit"


def test_main_tabs(mock_app):
    app, frame = mock_app

    tab = frame.winfo_children()[0]
    button = frame.winfo_children()[1]

    tab = cast(customtkinter.CTkTabview, tab)
    button = cast(customtkinter.CTkButton, button)

    # Assert current view
    assert tab.get() == "Backup"

    # Select and assert 'Restore' view
    tab.set("Restore")
    assert tab.get() == "Restore"

    # Assert exit button
    assert button.cget("text") == "Exit"
