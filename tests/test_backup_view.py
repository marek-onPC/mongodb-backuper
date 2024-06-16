from typing import Any, Generator, cast
import pytest
import customtkinter
from gui import backup_view
from unittest import mock
from unittest.mock import MagicMock

@pytest.fixture
def mock_app() -> Generator[tuple[customtkinter.CTk, customtkinter.CTkFrame], Any, None]:
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    
    app = customtkinter.CTk()
    app.title("MongoDB backuper")
    app.geometry("800x640")
    tab = customtkinter.CTkTabview(master=app)
    frame = backup_view.backup_view(root_element=tab)

    yield app, frame
    
    app.destroy()

@pytest.mark.parametrize(
    "test_db_url, test_db_name",
    [
        pytest.param(
            "test_connection_url",
            "test_db_name",
            id="Initate database backup",
        )
    ]
)
@mock.patch("commands.database_backup.database_backup")
def test_backup_view(
    mock_database_backup: MagicMock,
    mock_app: Generator[tuple[customtkinter.CTk, customtkinter.CTkFrame], Any, None],
    test_db_url: str,
    test_db_name: str,
):
    mock_database_backup.return_value = None
    app, frame = mock_app

    db_uri_input = frame.winfo_children()[0]
    db_uri_input = cast(customtkinter.CTkEntry, db_uri_input)

    db_name_input = frame.winfo_children()[1]
    db_name_input = cast(customtkinter.CTkEntry, db_name_input)

    backup_button = frame.winfo_children()[2]
    backup_button = cast(customtkinter.CTkButton, backup_button)

    # Assert UI
    assert db_uri_input._placeholder_text == "MondoDB connection URL"
    assert db_name_input._placeholder_text == "Database name"
    assert backup_button.cget("text") == "Prepare DB backup"

    # Type values in input
    db_uri_input.insert(0, test_db_url)
    db_name_input.insert(0, test_db_name)

    assert db_uri_input.get() == test_db_url
    assert db_name_input.get() == test_db_name

    backup_button.invoke()

    mock_database_backup.assert_called_once_with(test_db_url, test_db_name)
