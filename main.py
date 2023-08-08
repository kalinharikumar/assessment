import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
import random

# Download NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Read paragraph from text file
with open('paragraph.txt', 'r') as file:
    paragraph = file.read()

# Tokenize the paragraph into sentences
sentences = sent_tokenize(paragraph)

# Rest of the code remains the same
# ... (including the rest of the code from the previous response)

# Collect MCQs, options, and correct answers
mcq_data = []

# Identify sentence patterns, keywords, and generate MCQ options in each sentence
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

# Print collected MCQ data
for i, mcq in enumerate(mcq_data):
    print(f"MCQ {i+1}:")
    print(f"   Sentence: '{mcq['sentence']}'")
    print(f"   Pattern: {mcq['pattern']}")
    print(f"   Options: {mcq['options']}")
    print(f"   Correct Answers: {mcq['correct_answers']}\n")
