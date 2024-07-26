# generated from ChatGpt to understand the code BuildDictionary.py
import json
from pathlib import Path


class NheengatuProcessor:
    # Set the base directory to the current working directory
    BASE_DIR = Path.cwd() / "data"
    ALTDIR = Path.cwd() / "data"
    if not BASE_DIR.exists():
        BASE_DIR = ALTDIR
    INFILE = BASE_DIR / "glossary.txt"
    GLOSSARY = BASE_DIR / "glossary.json"
    LEXICON = BASE_DIR / "lexicon.json"

    NFIN = "NFIN"
    ARCHAIC = "ARCH"
    IMP = "IMP"
    AUX = "aux."
    IMPERS = "(impess.)"
    VSUFF = "v. suf."
    COP = "cop."

    PLURALIZABLE = ("N", "REL")

    TAGSET = """
    adj.\tA\tadjetivo
    adv.\tADV\tadvérbio
    conj.\tCONJ\tconjunção
    s.\tN\tsubstantivo comum
    pron.\tPRON\tpronome de 1ª classe
    pron. dem.\tDEM\tpronome demostrativo
    v.\tV\tverbo de 1ª classe
    v. suf.\tVSUFF\tverbo sufixal não-flexionável
    """

    def __init__(self):
        self.MAPPING = self.build_mapping()

    @staticmethod
    def build_mapping():
        table = []
        mapping = {}
        for l in NheengatuProcessor.TAGSET.strip().split("\n"):
            table.append(l.split("\t"))
        for line in table:
            mapping[line[0]] = line[1]
        return mapping

    @staticmethod
    def load_json(filepath):
        with open(filepath, encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def save_json(data, filepath):
        with open(filepath, "w", encoding="utf-8") as write_file:
            json.dump(data, write_file, indent=4, ensure_ascii=False)

    def parse_prefs(self, word):
        prefs = {"yu": "REFL", "mu": "CAUS"}
        i = 0
        features = []
        persnum = self.get_persnum()
        entry = {}

        for k, v in persnum.items():
            if word[i:].startswith(k):
                i = len(k)
                parts = v.split("+")
                entry["person"] = parts[0]
                if len(parts) == 2:
                    entry["number"] = parts[1]
                break

        for k, v in prefs.items():
            if word[i:].startswith(k):
                i += len(k)
                features.append(v)

        entry["lemma"] = word[i:]
        if features:
            entry["pref"] = "+".join(features)
        return entry

    @staticmethod
    def get_persnum():
        return {
            "a": "1+SG",
            "xa": "ARCH+1+SG",
            "ha": "1+SG",
            "re": "2+SG",
            "e": "IMP+2+SG",
            "u": "3",
            "ya": "1+PL",
            "pe": "2+PL",
            "ta": "3+PL",
            "tau": "3+PL",
        }

    def conjugate_verb(self, lemma, pos="V"):
        persnum = self.get_persnum()
        forms = set()

        if lemma == "yuri":
            for pref, tag in persnum.items():
                if "3" not in tag:
                    forms.add(f"{pref}{lemma}\t{lemma}+{pos}+{tag}")
            forms.add(f"uri\t{lemma}+{pos}+3")
            forms.add(f"yuri\t{lemma}+{pos}+IMP+2")
            return forms

        for pref, tag in persnum.items():
            forms.add(f"{pref}{lemma}\t{lemma}+{pos}+{tag}")
        forms.add(f"{lemma}\t{lemma}+{pos}+NFIN")
        return forms


def main():
    processor = NheengatuProcessor()
    glossary = processor.load_json(NheengatuProcessor.GLOSSARY)
    lexicon = processor.load_json(NheengatuProcessor.LEXICON)

    # Further processing and usage of processor methods
    # Example: conjugate verb 'yuri'
    forms = processor.conjugate_verb("yuri")
    for form in forms:
        print(form)


if __name__ == "__main__":
    main()
