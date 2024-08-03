import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = 'https://www.stadafa.com/2021/09/every-worlde-word-so-far-updated-daily.html'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the container with the Wordle words
content = soup.get_text()

# Split the content by newlines to process each line
lines = content.split('\n')

# Open a text file to save the extracted words
with open('wordle_words.txt', 'w') as file:
    for line in lines:
        if line.strip().startswith('1'):  # Check if the line starts with a number
            parts = line.split('. ')
            if len(parts) > 1:
                number = parts[0].strip()
                word = parts[1].split(' ')[0].strip()
                file.write(f'{number}. {word}\n')

print("Wordle words extracted and saved to wordle_words.txt")
