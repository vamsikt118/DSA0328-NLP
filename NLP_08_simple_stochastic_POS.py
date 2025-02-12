import nltk
from nltk.corpus import treebank
from collections import Counter, defaultdict
nltk.download('treebank')
tagged_sentences = treebank.tagged_sents()
word_tag_counts = defaultdict(Counter)
for sentence in tagged_sentences:
    for word, tag in sentence:
        word_tag_counts[word.lower()][tag] += 1
def stochastic_pos_tagger(sentence):
    tokens = sentence.split()
    tagged_sentence = []
    for token in tokens:
        if token.lower() in word_tag_counts:
            best_tag = word_tag_counts[token.lower()].most_common(1)[0][0]
        else:
            best_tag = 'NN' 
        tagged_sentence.append((token, best_tag))
    return tagged_sentence
text = input("Enter a sentence: ")
print("POS Tagged Output:", stochastic_pos_tagger(text))
