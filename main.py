import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
import random

with open('c1.txt', 'r') as file:
    paragraph = file.read()

sentences = sent_tokenize(paragraph)
mcq_data = []

for i, sentence in enumerate(sentences):
    pattern, keywords = recognize_and_extract(sentence)
    options = generate_mcq_options(keywords)
    
    if options:
        mcq_data.append({
            'sentence': sentence,
            'pattern': pattern,
            'options': options,
            'correct_answers': keywords[:2]
        })

for i, mcq in enumerate(mcq_data):
    print(f"MCQ {i+1}:")
    print(f"   Sentence: '{mcq['sentence']}'")
    print(f"   Pattern: {mcq['pattern']}")
    print(f"   Options: {mcq['options']}")
    print(f"   Correct Answers: {mcq['correct_answers']}\n")
