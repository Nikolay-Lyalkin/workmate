import csv
from collections import defaultdict

from tabulate import tabulate


def read_csv_file(files: list) -> list[dict]:
    """Функция чтения CSV файлов"""
    entrance_data = defaultdict(list)
    for file_path in files:
        try:
            with open(file_path, "r", encoding="UTF-8") as file:
                reader = csv.DictReader(file)

                if "position" not in reader.fieldnames or "performance" not in reader.fieldnames:
                    raise ValueError(
                        f"Файл {file_path} должен содержать колонки 'position' и 'performance'."
                    )

                for row in reader:
                    entrance_data[row.get("position")].append(float(row.get("performance")))

        except FileNotFoundError as e:
            print(f"Файл {file_path} не найден")
            raise e
        except ValueError as e:
            print(f"{e}")
            raise e
    report_data = []

    for position, performances in entrance_data.items():
        avg_performance = round(sum(performances) / len(performances), 2)
        report_data.append({"position": position, "performance": avg_performance})
    report_data.sort(key=lambda x: x["performance"], reverse=True)
    return report_data


def write_csv_file(report_data: list[dict], report_file: str):
    """Функция записи CSV файлов"""
    with open(report_file, "w", encoding="UTF-8") as file:
        fieldnames = ["position", "performance"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in report_data:
            writer.writerow(item)
        print(tabulate(report_data, headers="keys", tablefmt="presto"))
