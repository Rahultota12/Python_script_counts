import requests
from bs4 import BeautifulSoup
import json


url = input("Enter the URL of the static website: ")    # Input the URL of the static website


# Send a request to the website and get the HTML content
response = requests.get(url)         
soup = BeautifulSoup(response.content, 'html.parser')

text = soup.get_text()

# Split the text into words
words = text.split()

# Count the number of unique and repeated words
unique_words = set(words)
repeated_words = {}
for word in words:
    if word in repeated_words:
        repeated_words[word] += 1
    else:
        repeated_words[word] = 1

# Print the results terminal
print("Number of unique words:", len(unique_words))
print("Number of repeated words:", len(repeated_words))

# Store the results in a JSON file
results = {
    "unique_words": len(unique_words),
    "repeated_words": len(repeated_words),
    "word_counts": repeated_words
}

# Open json file
with open("results.json", "w") as f:
    json.dump(results, f)
