from pathlib import Path


class Config:
    DATA_DIR = Path.cwd() / "data"
    UD_DIR = DATA_DIR / "corpus" / "universal_dependencies"
    DB_PATH = DATA_DIR / "database_growth.db"
