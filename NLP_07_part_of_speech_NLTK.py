import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
text = "Hello myself Amritesh Prakash"
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)
print("POS Tags:", pos_tags)
