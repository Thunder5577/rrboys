from transformers import pipeline 
 
# Load the summarization pipeline from Hugging Face 
summarizer = pipeline("summarization") 
 
# Sample long passage to summarize 
long_text = """ 
In recent years, advancements in artificial intelligence (AI) have revolutionized the way industries operate, bringing about significant transformations in fields such as healthcare, finance, and manufacturing. AI technologies, including machine learning, natural language processing, and computer vision, have been integrated into various business processes, leading to improved efficiency, enhanced decision-making, and better customer experiences. However, the rapid growth of AI also raises concerns related to ethics, privacy, and the potential for job displacement. As AI continues to evolve, it is crucial for society to find a balance between embracing technological innovations and addressing the challenges they bring. Policymakers, industry leaders, and researchers must collaborate to establish guidelines that ensure the responsible development and deployment of AI systems, safeguarding human rights and promoting social well-being. 
""" 
 
# Obtain the summary using the summarization pipeline
# Setting do_sample=False ensures deterministic output (same result every time)
summary = summarizer(long_text, max_length=150, min_length=50, do_sample=False) 
 
# Print the summarized text 
print("Summary:") 
print(summary[0]['summary_text'])
