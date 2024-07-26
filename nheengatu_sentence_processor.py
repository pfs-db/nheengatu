# generated from chatgpt to understand the code AnnotateConllu.py
class Token:
    def __init__(
        self, form, lemma=None, upos=None, xpos=None, feats=None, head=None, deprel=None
    ):
        self.form = form
        self.lemma = lemma
        self.upos = upos
        self.xpos = xpos
        self.feats = feats if feats else {}
        self.head = head
        self.deprel = deprel

    def __str__(self):
        return f"{self.form}({self.upos})"


class Sentence:
    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.tokenize()

    def tokenize(self):
        words = self.text.split()
        for i, word in enumerate(words):
            self.tokens.append(Token(form=word))

    def annotate_tokens(self):
        for token in self.tokens:
            # Simplified POS tagging example
            if token.form.endswith("a"):
                token.upos = "NOUN"
            elif token.form.endswith("e"):
                token.upos = "VERB"
            else:
                token.upos = "OTHER"

            # Simplified lemmatization example
            token.lemma = token.form.lower()

    def annotate_dependencies(self):
        # Simplified dependency parsing example
        if self.tokens:
            self.tokens[0].deprel = "root"
            self.tokens[0].head = 0
            for i in range(1, len(self.tokens)):
                self.tokens[i].deprel = "dep"
                self.tokens[i].head = 1

    def __str__(self):
        return " ".join([str(token) for token in self.tokens])


# Example usage
text = "Kwá sera waá piranha"
sentence = Sentence(text)
sentence.annotate_tokens()
sentence.annotate_dependencies()
print(sentence)
