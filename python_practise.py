import os
import logging

text = "The big brown fox jumped from a high fence. He is moving very fast."
words = text.split(" ")
logging.debug(words)

len_words = [len(i) for i in words]
print(len_words)

wordlen = set(len_words)
print(wordlen)
wordlen = sorted(wordlen, reverse=True)
print(wordlen)
top_3_len = wordlen[0:3]
print(top_3_len)

top_3_words = []
for i in words:
    if len(i) == top_3_len[0]:
        print(i)
        top_3_words.append(i)
        top_3_len.remove(top_3_len[0])
        print(top_3_words)
print(top_3_words)



