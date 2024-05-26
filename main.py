from src.common_paths import module_path
import src.Nheengatagger as nh
import sys
import os, sys, datetime
from src.BuildDictionary import loadLexicon
from src.common_paths import module_path
import src.common_paths as cp
import argparse


def handle_args():
    """tmp function to show how the command lines interaction could be used"""
    parser = argparse.ArgumentParser(
        prog="nheengatu",
        description="Automatically POS-tagged by Nheengatagger",
        epilog="Text at the bottom of help",
    )
    parser.add_argument("infile")
    return parser


def main():
    parser = handle_args()
    args = parser.parse_args()

    DICTIONARY = nh.buildDictionary(cp.LEXICON_PATH)
    WE = nh.extractMWEs(DICTIONARY)
    print(cp.MESSAGE)
    lines = []
    with open(args.infile) as f:
        lines = f.readlines()
    nh.tagText(lines)


if __name__ == "__main__":
    main()
