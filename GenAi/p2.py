import gensim.downloader as api 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.decomposition import PCA 
from sklearn.manifold import TSNE 
 
model = api.load("word2vec-google-news-300") 
 
sports_words = ['football', 'basketball', 'soccer', 'tennis', 'baseball', 'hockey', 'athlete', 'coach', 'stadium', 'referee'] 
 
word_vectors = np.array([model[word] for word in sports_words]) 


pca = PCA(n_components=2) 
pca_result = pca.fit_transform(word_vectors) 
 

plt.figure(figsize=(8, 6)) 
 
for i, word in enumerate(sports_words): 
    plt.scatter(pca_result[i, 0], pca_result[i, 1]) 
 
    plt.text(pca_result[i, 0] + 0.1, pca_result[i, 1] + 0.1, word, fontsize=12) 
 

 
plt.title('Word Embeddings for Sports Domain (PCA)') 
plt.xlabel('PCA Component 1') 
plt.ylabel('PCA Component 2') 
plt.grid(True) 
plt.show() 

input_word = 'soccer' 
 

similar_words = model.most_similar(input_word, topn=5) 
 

print(f"Top 5 words similar to '{input_word}':") 
for word, similarity in similar_words: 
    print(f"{word}: Similarity = {similarity:.4f}") 