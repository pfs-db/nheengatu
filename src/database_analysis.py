import json
from pathlib import Path
import pandas as pd


def load_json(filepath):
    with open(filepath, "r") as file:
        return json.load(file)


# Normalize glossary JSON data
def normalize_json_data(json_data):
    """Ensure all dictionaries in the JSON data have the same keys."""
    all_keys = set().union(*(d.keys() for d in json_data if isinstance(d, dict)))
    normalized_data = [{key: d.get(key, None) for key in all_keys} for d in json_data]
    return normalized_data


# Normalize lexicon JSON data
def normalize_lexicon_data(json_data):
    """Convert lexicon JSON data to a list of dictionaries with consistent keys."""
    normalized_data = []
    for term, details in json_data.items():
        for detail in details:
            entry = {"term": term, "lemma": detail[0], "pos": detail[1]}
            normalized_data.append(entry)
    return normalized_data


def save_to_csv(data, filepath):
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)


def analyze_data(glossary_df, lexicon_df, data_dir):
    # Basic Frequency Analysis
    lexicon_freq = lexicon_df["lemma"].value_counts()
    glossary_freq = glossary_df["lemma"].value_counts()

    # Display the most common terms
    print("Most common terms in Lexicon:")
    print(lexicon_freq.head(10))

    print("\nMost common terms in Glossary:")
    print(glossary_freq.head(10))

    # Comparative Analysis
    common_terms = set(lexicon_df["lemma"]).intersection(set(glossary_df["lemma"]))
    print(f"Number of common terms: {len(common_terms)}")

    # Save the common terms to a CSV file
    common_terms_df = pd.DataFrame(list(common_terms), columns=["lemma"])
    common_terms_df.to_csv(data_dir / "common_terms.csv", index=False)


def analyze_database(data_dir):
    data_dir = Path(data_dir)

    # Load JSON files
    glossary = load_json(data_dir / "glossary.json")
    lexicon = load_json(data_dir / "lexicon.json")

    # Normalize JSON data
    glossary = normalize_json_data(glossary)
    lexicon = normalize_lexicon_data(lexicon)

    # Save normalized data to CSV
    save_to_csv(glossary, data_dir / "glossary.csv")
    save_to_csv(lexicon, data_dir / "lexicon.csv")

    # Load data into DataFrames for analysis
    glossary_df = pd.DataFrame(glossary)
    lexicon_df = pd.DataFrame(lexicon)

    # Perform analysis
    analyze_data(glossary_df, lexicon_df, data_dir)
