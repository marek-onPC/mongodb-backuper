from typing import Any, Generator, cast
import pytest
import customtkinter
from gui import restore_view
from unittest import mock
from unittest.mock import MagicMock


TEST_FILE = {"test_key": "test_value"}


@pytest.fixture
def mock_app() -> Generator[tuple[customtkinter.CTk, customtkinter.CTkFrame], Any, None]:
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    
    app = customtkinter.CTk()
    app.title("MongoDB backuper")
    app.geometry("800x640")
    tab = customtkinter.CTkTabview(master=app)
    frame = restore_view.restore_view(root_element=tab)

    yield app, frame
    
    app.destroy()


def _mock_backup_file_func():
    global backup_db_file

    backup_db_file = TEST_FILE


@pytest.mark.parametrize(
    "test_db_url, test_db_name",
    [
        pytest.param(
            "test_connection_url",
            "test_db_name",
            id="Initate database restore",
        )
    ]
)
@mock.patch("gui.restore_view._select_backup_file")
@mock.patch("commands.database_restore.database_restore")
def test_restore_view(
    mock_database_restore: MagicMock,
    mock_select_backup_file: MagicMock,
    mock_app: Generator[tuple[customtkinter.CTk, customtkinter.CTkFrame], Any, None],
    test_db_url: str,
    test_db_name: str,
):
    mock_database_restore.return_value = None
    mock_select_backup_file.side_effect = _mock_backup_file_func
    app, frame = mock_app

    db_uri_input = frame.winfo_children()[0]
    db_uri_input = cast(customtkinter.CTkEntry, db_uri_input)

    db_name_input = frame.winfo_children()[1]
    db_name_input = cast(customtkinter.CTkEntry, db_name_input)

    file_button = frame.winfo_children()[2]
    file_button = cast(customtkinter.CTkButton, file_button)

    restore_button = frame.winfo_children()[3]
    restore_button = cast(customtkinter.CTkButton, restore_button)

    # Assert UI
    assert db_uri_input._placeholder_text == "MondoDB connection URL"
    assert db_name_input._placeholder_text == "Database name"
    assert file_button.cget("text") == "Select file with DB backup"
    assert restore_button.cget("text") == "Restore DB backup"

    # Type values in input
    db_uri_input.insert(0, test_db_url)
    db_name_input.insert(0, test_db_name)

    assert db_uri_input.get() == test_db_url
    assert db_name_input.get() == test_db_name

    file_button.invoke()
    mock_select_backup_file.assert_called_once()

    restore_button.invoke()

    assert backup_db_file == TEST_FILE

    mock_database_restore.assert_called_once_with(test_db_url, test_db_name, None)
