import flask
import nltk
import pandas as pd
from nltk import word_tokenize
from flask import Flask, request
import json

app = Flask(__name__)


class WordPreprocess:

    def __init__(self):
        self.num_of_words = 2

    def top_words(self, text):
        word_tokens = word_tokenize(text)
        word_tokens = [word for word in word_tokens if len(word) > 2]
        textdf = pd.DataFrame({'words': word_tokens})
        count_dict = dict(textdf.words.value_counts())
        top_words = list(count_dict.values())[:self.num_of_words]
        return top_words

    def least_words(self, text):
        word_tokens = word_tokenize(text)
        word_tokens = [word for word in word_tokens if len(word) > 2]
        text_df = pd.DataFrame({'words': word_tokens})

        count_dict = dict(text_df.value_counts())
        least_words = list(count_dict.values())[-self.num_of_words]
        return least_words


if __name__ == "__main__":
    wordprocessobj = WordPreprocess()
    wordprocessobj.num_of_words = 3

    text = """A few days before Hurricane Irma hit South Florida, I received a query on Twitter from a graphic designer named Eric Bailey.Has anyone researched news sites capability to provide low-bandwidth communication of critical info during crisis situations? he asked.The question was timely — two days la These text-only sites — which used to be more popular in the early days of the Internet,when networks were slower and bandwidth was at a premium – are incredibly useful, and not just during natural disasters. T
hey load much faster, don’t contain any pop-ups or ads or autoplay videos, and help people with low bandwidth or limited Internet access. They’re also beneficial for people with visual impairments who use screen readers to navigate the Internet."""

    top_words = wordprocessobj.top_words
