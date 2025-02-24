import collections
import random
import spacy

nlp = spacy.load("en_core_web_sm")

class SimpleBabbler():
    # Inspired by:
    #     https://gist.github.com/benhoyt/619cf3113866450aa31d8a2c1f8e01dc
    #     https://benhoyt.com/writings/markov-chain/
    def __init__(self, inspiration_text):
        self.inspiration_text = inspiration_text
        self.possibles = collections.defaultdict(list)
        self.inspire_babbler()

    def inspire_babbler(self):
        word1 = word2 = ''
        for word in self.inspiration_text.split():
            self.possibles[word1, word2].append(word)
            word1, word2 = word2, word
        self.possibles[word1, word2].append('')
        self.possibles[word2, ''].append('')

    def babble(self, word_count):
        word1, word2 = random.choice([w for w in self.possibles if w[0][:1].isupper()])
        output = [word1, word2]
        for _ in range(word_count):
            next_word = random.choice(self.possibles[word1, word2])
            output.append(next_word)
            word1, word2 = word2, next_word
        return ' '.join(output)


class GuidedBabbler():
    replace_tags = ['NN', 'NNS', 'VBN', 'JJ', 'MD']

    def __init__(self, inspiration_text):
        self.inspire(inspiration_text)

    def inspire(self, insp_text):
        doc = nlp(insp_text)
        look_here = [[t.text, t.pos_, t.tag_, t.dep_] for t in doc]
        print("break")
