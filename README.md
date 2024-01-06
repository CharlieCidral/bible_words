# Bible Word and Phrase Counter

This project contains a Python script that parses an HTML file of the Bible and creates a treemap visualization of the most common words and phrases.
### Words
![image](https://github.com/CharlieCidral/bible_words/assets/69029099/796b4b3b-0b63-4017-a211-25d5b9ab6a3c)


### Phrases
![image](https://github.com/CharlieCidral/bible_words/assets/69029099/50049e6d-b974-4456-8419-c0857eb8d361)

## The phrase can be improve with ML:
  Here’s a high-level idea of how this could be done:

  - Preprocess the text: This could involve cleaning the text, removing stop words, and possibly lemmatizing words.
  
  - Convert sentences into vectors: Use an NLP model to convert each sentence into a vector. This could be a simple Bag-of-Words model, TF-IDF, or more complex models like Word2Vec, GloVe, BERT, etc.
  
  - Calculate similarity: For each sentence, calculate its similarity to all other sentences. This could be done using cosine similarity, which is a common measure for the similarity between vectors.
  
  - Group sentences: Based on their similarities, group sentences together. This could be done using a clustering algorithm like K-means.
  
  - Count groups: Instead of counting identical sentences, count the number of sentences in each group.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You need to have Python installed on your machine. You also need the following Python libraries:

- BeautifulSoup
- collections
- re
- matplotlib
- squarify

You can install these libraries using pip:

```
pip install beautifulsoup4 matplotlib squarify
```

### Running the Script
To run the script, navigate to the directory containing the script and run the following command:
```
python words.py
```
or
```
python phrases.py
```

## Authors
Charlie

## License
This project is licensed under the MIT License.

## Acknowledgments
Thanks to OpenAI for providing the initial guidance for this project.
