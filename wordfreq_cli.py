import sys

from textstats.freq import top_words

text = open(sys.argv[1], encoding="utf-8").read()
for word, count in top_words(text, int(sys.argv[2])):
    print(word, count)
