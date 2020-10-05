# importing the necessary libraries
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

#adding new line to punctuation
punctuation = punctuation + '\n'


# Getting the list of all the stop words
stop_words = list(STOP_WORDS)

# Loading the NLP model from spacy
nlp = spacy.load('en_core_web_sm')

#fitting the text to model
def model(text):
    doc = nlp(text)
    return doc


#word tokenization 
def word_tokenization(doc):
    tokens = [tokens.text for tokens in doc]
    return tokens

#generating frequency of each word in the text
def generate_word_frequency(doc):    
    word_frequency = {}
    for word in doc:
        if word.text.lower() not in stop_words:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequency.keys():
                    word_frequency[word.text] = 1
                else:
                    word_frequency[word.text] += 1
    return word_frequency

#normalization of the word frequency
def normalization_word_frequency(word_frequency):
    max_frequency = max(word_frequency.values())
    for word in word_frequency.keys():
        word_frequency[word] = word_frequency[word]/max_frequency
    return word_frequency

#sentence tokenization
def sentence_tokenization(doc):
    sentence_tokens = [sent for sent in doc.sents]
    return sentence_tokens


#generating sentence scores for each sentence
def generate_sentence_scores(sentence_tokens, word_frequency):
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequency.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequency[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequency[word.text.lower()]
    return sentence_scores

#setting summary length
def generate_summary_length(sentence_tokens):
    summary_length = int(len(sentence_tokens)*0.3)
    return summary_length

#generating sentence summary
def generate_summary(summary_length, sentence_scores):
    summary_sentences = nlargest(summary_length, sentence_scores, key=sentence_scores.get)
    summary_words = [words.text for words in summary_sentences]
    final_summary = ' '.join(summary_words)
    return final_summary

def main(text):
    doc = model(text)
    tokens = word_tokenization(doc)
    word_frequency = generate_word_frequency(doc)
    normalized_word_frequency = normalization_word_frequency(word_frequency)
    sentence_tokens = sentence_tokenization(doc)
    sentence_scores = generate_sentence_scores(sentence_tokens, normalized_word_frequency)
    summary_length = generate_summary_length(sentence_tokens)
    final_summary = generate_summary(summary_length, sentence_scores)
    return final_summary




