import json


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_conllu(file_path):
    sentences = []
    with open(file_path, "r", encoding="utf-8") as file:
        sentence = []
        for line in file:
            line = line.strip()
            if line == "":
                if sentence:
                    sentences.append(sentence)
                    sentence = []
            elif not line.startswith("#"):
                sentence.append(line.split("\t"))
        if sentence:
            sentences.append(sentence)
    return sentences


def load_all_conllu(directory):
    return [load_conllu(file) for file in directory.glob("*.conllu")]
