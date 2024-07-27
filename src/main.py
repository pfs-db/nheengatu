from data_preprocessing import preprocess_data
import argparse
import config
from database_analysis import analyze_database


def main():
    parser = argparse.ArgumentParser(description="Your Project CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Database analysis command
    db_parser = subparsers.add_parser("analyze_db", help="Analyze the database")
    db_parser.add_argument(
        "--data-dir",
        type=str,
        default=config.Config.DATA_DIR,
        help="Directory containing data files",
    )

    # Data preprocessing command
    preprocess_parser = subparsers.add_parser("preprocess", help="Preprocess data")
    preprocess_parser.add_argument(
        "--data-dir",
        type=str,
        default=config.Config.DATA_DIR,
        help="Directory containing data files",
    )

    args = parser.parse_args()

    if args.command == "analyze_db":
        analyze_database(args.data_dir)
    elif args.command == "preprocess":
        preprocess_data(args.data_dir)
    # Add more conditions for other commands here


if __name__ == "__main__":
    main()
