import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = 'https://www.ef.edu/english-resources/english-vocabulary/top-3000-words/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the container with the words
words_container = soup.find('div', class_='field-item even')
words = words_container.get_text(separator="\n").split()

# Save the words to a text file
with open('top_3000_words.txt', 'w') as file:
    for word in words:
        file.write(word + '\n')

print("Top 3000 words extracted and saved to top_3000_words.txt")
