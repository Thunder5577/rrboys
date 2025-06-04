import gensim.downloader as api 
from gensim.models import KeyedVectors
model = api.load("word2vec-google-news-300") 
king_vector = model['king'] 
man_vector = model['man'] 
woman_vector = model['queen'] 
result_vector = king_vector - man_vector + woman_vector 
result_word = model.most_similar([result_vector], topn=1) 
print("Resulting word: ", result_word)