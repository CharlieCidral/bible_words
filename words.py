from bs4 import BeautifulSoup
from collections import Counter
import re
import matplotlib.pyplot as plt
import squarify
import matplotlib as mpl

# your HTML file path
html_file = "D:\\programClass\\Python\\Bible words and phrases\\bible.html"

# read the HTML file
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# parse HTML
soup = BeautifulSoup(html, 'html.parser')

# find all text
texts = soup.findAll(string=True)

# join all text
words = ' '.join(texts)

# remove non-alphabetic characters
words = re.sub(r'[^a-zA-Z\s]', '', words)

# split into list of words
word_list = words.lower().split()

# count words
word_count = Counter(word_list)

# get the 33 most common words
most_common_words = word_count.most_common(100)

# separate words and counts into two lists
words, counts = zip(*most_common_words)

# create labels with word and count
labels = [f'{word} ({count})' for word, count in zip(words, counts)]

# crie um mapa de cores
cmap = mpl.colormaps['twilight']  # use 'viridis', 'plasma', 'inferno', 'magma', 'cividis', etc.

# create two subplots
fig, axs = plt.subplots(2, figsize=(10, 10))

# create treemap for the 50 most common words
squarify.plot(sizes=counts[:50], label=labels[:50], alpha=.7, color=cmap([x/max(counts[:50]) for x in counts[:50]]), ax=axs[0])
axs[0].axis('off')
axs[0].set_title('Top 50 Most Common Words')

# create treemap for the next 50 most common words
squarify.plot(sizes=counts[50:], label=labels[50:], alpha=.7, color=cmap([x/max(counts[50:]) for x in counts[50:]]), ax=axs[1])
axs[1].axis('off')
axs[1].set_title('51 to 100 Most Common Words')

plt.tight_layout()
plt.show()
