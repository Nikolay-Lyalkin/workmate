import argparse

from services import read_csv_file, write_csv_file


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", required=True)
    args = parser.parse_args()
    data_report = read_csv_file(args.files)
    result = write_csv_file(data_report, args.report)


if __name__ == "__main__":
    main()
