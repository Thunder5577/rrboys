
import fitz  
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
pdf_path = 'IPC.pdf'
doc = fitz.open(r"C:\Users\Keshav\Desktop\IPC.pdf")


ipc_text = ""
for page_num in range(doc.page_count):
    page = doc.load_page(page_num)
    ipc_text += page.get_text()
doc.close()
sentences = ipc_text.split(".")
sentences = [s.strip() for s in sentences if s.strip()]
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
ipc_embeddings = model.encode(sentences)
def query_ipc_document(query, top_k=3):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, ipc_embeddings)
    top_k_indices = similarities[0].argsort()[-top_k:][::-1]
    top_k_sentences = [sentences[i] for i in top_k_indices]
    return top_k_sentences
query = input("Ask a question about the Indian Penal Code: ")
answer = query_ipc_document(query)
print("\nHere are the top responses from the IPC document:\n")
for idx, sentence in enumerate(answer):
    print(f"{idx+1}. {sentence}")
