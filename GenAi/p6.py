from transformers import pipeline 

# Load sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis") 

# Sample sentences
sentences = [ 
    "I love using Hugging Face models for natural language processing!", 
    "The weather today is quite gloomy and depressing.", 
    "I'm excited about the upcoming holidays." 
] 

# Run sentiment analysis
results = sentiment_analyzer(sentences) 

# Print results
for sentence, result in zip(sentences, results): 
    print(f"Sentence: {sentence}") 
    print(f"Sentiment: {result['label']}, Confidence: {result['score']:.4f}\n")
