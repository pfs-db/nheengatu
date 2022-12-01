from src.common_paths import module_path
import src.Nheengatagger as nh
import sys
import os, sys, datetime
from src.BuildDictionary import loadLexicon
from src.common_paths import module_path
import src.common_paths as cp


def main(infile):
    DICTIONARY = nh.buildDictionary(cp.LEXICON_PATH)
    WE = nh.extractMWEs(DICTIONARY)
    print(cp.MESSAGE)
    lines = []
    with open(infile) as f:
        lines = f.readlines()
    nh.tagText(lines)


if __name__ == "__main__":
    main(sys.argv[1])  # TODO use argparse module
