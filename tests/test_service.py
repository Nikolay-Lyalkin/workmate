from unittest.mock import MagicMock, mock_open, patch

from services import read_csv_file, write_csv_file


def test_read_csv_file():
    """Тест чтения CSV файла"""

    mock_rows = [
        {"position": "Backend Developer", "performance": "4.5"},
        {"position": "Frontend Developer", "performance": "3.9"},
        {"position": "Backend Developer", "performance": "4.8"},
        {"position": "Frontend Developer", "performance": "4.1"},
    ]

    with patch("builtins.open", mock_open()) as mock_file:
        with patch("csv.DictReader") as mock_reader:

            mock_reader_instance = MagicMock()
            mock_reader_instance.fieldnames = ["position", "performance"]
            mock_reader_instance.__iter__.return_value = iter(mock_rows)
            mock_reader.return_value = mock_reader_instance

            data = read_csv_file(["path_to_file.csv"])

            # Проверяем вызов open
            mock_file.assert_called_once_with("path_to_file.csv", "r", encoding="UTF-8")

            assert data == [
                {"position": "Backend Developer", "performance": 4.65},
                {"position": "Frontend Developer", "performance": 4.0},
            ]


def test_write_csv_file():
    """Тест записи CSV файла"""

    report_data = [
        {"position": "Developer", "performance": 4.5},
        {"position": "Manager", "performance": 4.8},
    ]

    with patch("builtins.open", mock_open()) as mock_file:

        write_csv_file(report_data, "test_report.csv")

        mock_file.assert_called_once_with("test_report.csv", "w", encoding="UTF-8")
