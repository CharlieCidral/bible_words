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
text = ' '.join(texts)

# convert to lowercase
text = text.lower()

# remove non-alphabetic characters except periods and spaces
text = re.sub(r'[^a-zA-Z\.,; ]', '', text)

# split into list of phrases using periods, commas, and semicolons as separators
phrase_list = re.split('[.,;]', text)

# strip extra spaces from each phrase
phrase_list = [phrase.strip() for phrase in phrase_list]

# count phrases
phrase_count = Counter(phrase_list)

# get the 100 most common phrases
most_common_phrases = phrase_count.most_common(20)

# separate phrases and counts into two lists
phrases, counts = zip(*most_common_phrases)

# create labels with phrase and count
labels = [f'{phrase} ({count})' for phrase, count in zip(phrases, counts)]

# create color map
cmap = mpl.colormaps['twilight']

# create two subplots
fig, axs = plt.subplots(2, figsize=(10, 10))

# create treemap for the 50 most common phrases
squarify.plot(sizes=counts[:10], label=labels[:10], alpha=.7, color=cmap([x/max(counts[:10]) for x in counts[:10]]), ax=axs[0])
axs[0].axis('off')
axs[0].set_title('Top 10 Most Common Phrases')

# create treemap for the next 50 most common phrases
squarify.plot(sizes=counts[10:], label=labels[10:], alpha=.7, color=cmap([x/max(counts[10:]) for x in counts[10:]]), ax=axs[1])
axs[1].axis('off')
axs[1].set_title('Next 10 Most Common Phrases')

plt.tight_layout()
plt.show()
