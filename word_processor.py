# Processing Linguistic Data
class WordParseProcessor:
    def __init__(self, mapping, pronouns, pluralizable, impers, vsuff, aux):
        self.MAPPING = mapping
        self.PRONOUNS = pronouns
        self.PLURALIZABLE = pluralizable
        self.IMPERS = impers
        self.VSUFF = vsuff
        self.AUX = aux

    def word_parse_pairs(self, glossary):
        pairs = set()
        for entry in glossary:
            lemma, pos, tags = self.get_lemma_pos_tags(entry, self.exclude_aux)
            rel = entry.get("rel")
            forms = set()
            if rel:
                tag = tags[0]
                l = len(rel)
                if l == 2:
                    forms.add((rel[0], f"{lemma}+{tag}+CONT"))
                    ncont = rel[1].split("/")
                    for form in ncont:
                        forms.add((form, f"{lemma}+{tag}+NCONT"))
                    if self.tag_nor_loc(tag):
                        forms.add((lemma, f"{lemma}+{tag}+ABS"))
                        pairs.update(self.make_number(forms))
                    else:
                        pairs.update(forms)
                elif l == 1:
                    pairs.add(f"{lemma}\t{lemma}+{tag}+CONT")
                    pairs.add(f"{rel[0]}\t{lemma}+{tag}+NCONT")
            else:
                for tag in tags:
                    if self.has_number_inflection(tag, lemma):
                        pairs.update(self.make_number([(lemma, f"{lemma}+{tag}")]))
                    elif tag == "V" and not self.is_impersonal(entry):
                        pairs.update(self.conjugate_verb(lemma, tag))
                    elif tag == "V3":
                        pairs.update(self.handle_v3(lemma, tag))
                    elif tag in self.PRONOUNS:
                        pairs.add(self.expand_pronoun(lemma, tag))
                    else:
                        pairs.add(f"{lemma}\t{lemma}+{tag}")
        return pairs

    def make_number(self, forms):
        entries = set()
        for form, parse in forms:
            entries.add(f"{form}\t{parse}+SG")
            entries.add(f"{form}-itá\t{parse}+PL")
            entries.add(f"{form}-etá\t{parse}+PL")
        return entries

    def is_impersonal(self, entry):
        return self.IMPERS in entry.get("gloss") or self.VSUFF in entry.get("pos")

    def get_lemma_pos_tags(self, entry, include_function):
        lemma = entry.get("lemma")
        pos = entry.get("pos")
        tags = self.extract_tags(pos, include_function)
        return lemma, pos, tags

    def extract_tags(self, pos, include_function):
        return [
            self.MAPPING.get(tag.strip())
            for tag in pos.split("/")
            if include_function(tag)
        ]

    def exclude_aux(self, tag):
        return self.AUX not in tag

    @staticmethod
    def tag_nor_loc(tag):
        return tag in ["N", "LOC"]

    def has_number_inflection(self, tag, lemma):
        if tag:
            if (
                tag in self.PLURALIZABLE
                or self.is_inflectable_dem(tag)
                or lemma in ("amú",)
            ):
                return True
        return False

    @staticmethod
    def is_inflectable_dem(tag):
        return tag.startswith("DEM") and not tag.endswith("N")

    def handle_v3(self, lemma, tag):
        forms = set()
        forms.add(f"{lemma}\t{lemma}+{tag}+NCONT")
        return forms

    def expand_pronoun(self, lemma, pos):
        feats = ""
        if pos in self.FIRST_CLASS_PRONOUNS:
            feats = self.first_class_pron()[lemma]
        elif pos in self.SECOND_CLASS_PRONOUNS:
            feats = self.second_class_pron()[lemma]
        return f"{lemma}\t{lemma}+{pos}+{feats}"

    @staticmethod
    def first_class_pron():
        return {
            "ixé": "1+SG",
            "indé": "2+SG",
            "iné": "2+SG",
            "aé": "3+SG",
            "yandé": "1+PL",
            "yané": "ARCH+1+PL",
            "penhẽ": "2+PL",
            "tá": "3+PL",
            "ta": "3+PL",
            "aintá": "3+PL",
            "indéu": "2+SG+DAT",
            "inéu": "2+SG+DAT",
            "yandéu": "1+PL+DAT",
            "yanéu": "1+PL+DAT",
            "ixéu": "1+SG+DAT",
            "penhemu": "2+PL+DAT",
        }

    @staticmethod
    def second_class_pron():
        return {
            "se": "1+SG",
            "xe": "1+SG",
            "ne": "2+SG",
            "i": "3+SG",
            "yané": "1+PL",
            "yandé": "ARCH+1+PL",
            "pe": "2+PL",
            "tá": "3+PL",
            "ta": "3+PL",
            "aintá": "3+PL",
        }
