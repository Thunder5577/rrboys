import gensim.downloader as api
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import random
import string
import nltk

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load the Word2Vec model
word_vectors = api.load("word2vec-google-news-300")

def get_similar_words(word, top_n=5):
    try:
        similar_words = word_vectors.most_similar(word, topn=top_n)
        return [w[0] for w in similar_words]
    except KeyError:
        return []

def generate_paragraph(seed_word, num_sentences=5):
    similar_words = get_similar_words(seed_word)
    if not similar_words:
        return "No similar words found."

    # Remove stopwords and punctuation from similar words
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in similar_words if word.lower() not in stop_words and word not in string.punctuation]

    if not filtered_words:
        return "No suitable similar words found after filtering."

    sentences = []
    for _ in range(num_sentences):
        random.shuffle(filtered_words)
        sentence_words = filtered_words[:random.randint(3, len(filtered_words))]
        sentence = f"Exploring the concept of '{seed_word}', we delve into its various facets, including {', '.join(sentence_words)}."
        sentences.append(sentence)

    return " ".join(sentences)

if __name__ == "__main__":
    seed_word = input("Enter a seed word: ")
    paragraph = generate_paragraph(seed_word)
    print("\nGenerated Paragraph:")
    print(paragraph)
