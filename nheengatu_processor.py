import json
from pathlib import Path
import re
from jsonschema import validate, ValidationError


class NheengatuProcessor:
    """This class will read a txt file and generate glossary.json and lexicon.json"""

    BASE_DIR = Path.cwd() / "data"
    ALTDIR = Path.cwd() / "data"
    if not BASE_DIR.exists():
        BASE_DIR = ALTDIR
    INFILE = BASE_DIR / "glossary.txt"
    GLOSSARY = BASE_DIR / "glossary.json"
    LEXICON = BASE_DIR / "lexicon.json"

    FIRST_CLASS_PRONOUNS = ["PRON", "PROND"]
    SECOND_CLASS_PRONOUNS = ["PRON2"]
    PRONOUNS = FIRST_CLASS_PRONOUNS + SECOND_CLASS_PRONOUNS

    # Define the schema for validation
    schema = {
        "type": "object",
        "properties": {
            "lemma": {"type": "string"},
            "pos": {"type": "string"},
            "gloss": {"type": "string"},
            "var": {"type": ["integer", "null"]},
        },
        "required": ["lemma", "pos", "gloss"],
    }

    def load_json(self, filepath):
        with open(filepath, encoding="utf-8") as f:
            return json.load(f)

    def save_json(self, data, filepath):
        with open(filepath, "w", encoding="utf-8") as write_file:
            json.dump(data, write_file, indent=4, ensure_ascii=False)

    def extract_lines(self, infile):
        """Reads lines from an input file, ignoring comments and empty lines."""
        return [
            line.strip()
            for line in open(infile, "r", encoding="utf-8").readlines()
            if not self.ignore(line)
        ]

    @staticmethod
    def ignore(line):
        line = line.strip()
        return line == "" or line.startswith("#")

    def build_glossary(self, entries):
        """Constructs a glossary from parsed entries, adding additional information such as relational forms and pronoun classifications."""
        glossary = []
        for entry in entries:
            # Custom processing logic here
            glossary.append(entry)
        return glossary

    # Validation function
    def validate_entry(self, entry):
        try:
            validate(instance=entry, schema=self.schema)
            return True, None
        except ValidationError as e:
            return False, str(e)

    # Parsing function
    def parse_text_to_json(self, infile, outfile):
        entries = []
        with open(infile, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    parts = re.split(r"\s*[\t-]\s*", line.strip())
                    if len(parts) >= 3:
                        entry = {
                            "lemma": parts[0],
                            "pos": parts[1],
                            "gloss": parts[2],
                            "var": (
                                int(parts[3])
                                if len(parts) > 3 and parts[3].isdigit()
                                else None
                            ),
                        }
                        valid, error = self.validate_entry(entry)
                        if valid:
                            entries.append(entry)
                        else:
                            print(f"Validation error in line '{line.strip()}': {error}")

        glossary = self.build_glossary(entries)
        self.save_json(glossary, outfile)


if __name__ == "__main__":
    p = NheengatuProcessor()
    p.parse_text_to_json(p.INFILE, p.GLOSSARY)
