# assessment
# Internship Assignment for NLP

Importing Libraries: Importing the required libraries. Using the NLTK library for natural language processing tasks and random for shuffling options.

Downloading NLTK Resources: The NLTK resources for tokenization and part-of-speech tagging are downloaded using the nltk.download() function.

Reading Paragraph from Text File: reads the content of a text file as paragraph.txt that will be processed to generate MCQs.

Tokenize the Paragraph: paragraph is tokenized into individual sentences using the sent_tokenize() function from NLTK.

Define Sentence Patterns: The code defines different sentence patterns and their corresponding part-of-speech tags. These patterns include declarative, interrogative, imperative, and exclamatory sentences.

Recognize Sentence Patterns and Extract Keywords: For each sentence in the paragraph, the code uses the defined sentence patterns to recognize the type of sentence. It also extracts keywords from the sentence by identifying nouns and proper nouns using part-of-speech tagging.

Generate MCQ Options: The generate_mcq_options() function takes the extracted keywords and generates MCQ options. It shuffles the keywords, selects two as correct options, and two more as wrong answers.

Collect MCQ Data: The code creates a list called mcq_data to store information about each generated MCQ, including the sentence, pattern, options, and correct answers.

Loop Through Sentences: The code iterates through each sentence in the paragraph. For each sentence, it recognizes the sentence pattern, extracts keywords, and generates MCQ options.

Print Collected MCQ Data: After processing all sentences, the code loops through the mcq_data list and prints the collected MCQ data, including the sentence, pattern, options, and correct answers.





