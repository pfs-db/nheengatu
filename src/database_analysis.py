from pathlib import Path
from data_loader import load_json, load_all_conllu
from database import create_db, log_db_sizes


def analyze_json(json_data):
    return len(json_data)


def analyze_conllu(conllu_data):
    return len(conllu_data)


def analyze_database(data_dir):
    data_dir = Path(data_dir)
    UD_DIR = data_dir / "corpus" / "universal_dependencies"
    DB_PATH = data_dir / "database_growth.db"

    # Load JSON files
    glossar = load_json(data_dir / "glossary.json")
    lexicon = load_json(data_dir / "lexicon.json")

    # Find all .conllu files in the specified directory
    conllu_data = load_all_conllu(UD_DIR)

    # Analyze data
    glossar_size = analyze_json(glossar)
    lexicon_size = analyze_json(lexicon)
    conllu_sizes = [analyze_conllu(data) for data in conllu_data]

    # Print sizes
    print(f"Glossar size: {glossar_size} entries")
    print(f"Lexicon size: {lexicon_size} entries")
    for i, size in enumerate(conllu_sizes):
        print(f"CoNLL-U file size: {size} sentences")

    # Log sizes to database
    create_db(DB_PATH)
    log_db_sizes(DB_PATH, glossar_size, lexicon_size)
