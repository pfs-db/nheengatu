import pandas as pd
import matplotlib.pyplot as plt
import sqlite3


def plot_growth_trend(db_path):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM database_growth", conn)
    conn.close()

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    plt.figure(figsize=(10, 6))
    plt.plot(df["timestamp"], df["glossar_size"], label="Glossar Size")
    plt.plot(df["timestamp"], df["lexicon_size"], label="Lexicon Size")
    plt.xlabel("Time")
    plt.ylabel("Entries")
    plt.title("Database Growth Over Time")
    plt.legend()
    plt.tight_layout()
    plt.show()
