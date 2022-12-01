from pathlib import Path
import sys, os
import datetime

if getattr(sys, "frozen", False):
    module_path = Path(sys.executable).absolute().parent.parent
else:
    module_path = Path(__file__).absolute().parent.parent

USER = os.path.expanduser("~")
DATA_PATH = module_path.joinpath("data")
DOCS_PATH = module_path.joinpath("docs")
LEXICON_PATH = DATA_PATH.joinpath("lexicon.json")
# Moving this variables else where
USER = os.path.expanduser("~")
PATH = os.path.join(USER, "complin/nheengatu/data")

LEXICONFILE = os.path.join(module_path, "lexicon.json")

# LEXICON = loadLexicon(LEXICON_PATH)
DASHES = ["‒", "–", "—", "―"]
PUNCTUATION = """.,;':?!“”"…()][}{"""
ELLIPSIS = "[...]"
XXXX = "xxxx"
ELIP = "ELIP"
OPERATOR = "Leonel Figueiredo de Alencar"
MESSAGE = f"""'''Automatically POS-tagged by Nheengatagger.
Operator: {OPERATOR}.
Date: {datetime.datetime.now().strftime("%c")}.
Metadata of the original corpus file reproduced below.'''
"""
NAMES = [
    "antônio",
    "barra",
    "catarina",
    "maria",
    "miguel",
    "paulo",
    "pedro",
    "rute",
    "são",
    "tefé",
    "josé",
    "joana",
    "jesus",
    "kristu",
    "deus",
    "kurukuí",
    "augusto",
    "yuruparí",
    "iahuixa",
    "buopé",
    "rairú",
    "isana",
    "pirayawara",
    "matapí",
    "uauhi",
    "uanskẽ",
    "porominare",
    "poronominare",
    "karu",
    "kukuí",
    "pitiápo",
]
