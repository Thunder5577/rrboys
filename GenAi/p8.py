# Step 1: Install required libraries
!pip install langchain cohere langchain-community

# Step 2: Import necessary libraries
import cohere
import getpass
from langchain import PromptTemplate
from langchain.llms import Cohere
from google.colab import drive

# Step 3: Mount Google Drive
drive.mount('/content/drive')

# Step 4: Set the correct file path
file_path = '/content/drive/MyDrive/Colab Notebooks/textfileForpgm8.txt'  # <-- Change to your actual filename

# Step 5: Read the text file
try:
    with open(file_path, 'r') as file:
        text_content = file.read()
    print("✅ File loaded successfully!")
except Exception as e:
    print("❌ Error loading file:", str(e))
    text_content = ""  # Prevent NameError in case of failure

# Step 6: Input Cohere API Key securely
COHERE_API_KEY = getpass.getpass("🔑 Enter your Cohere API Key: ")

# Step 7: Initialize Cohere LLM
cohere_llm = Cohere(cohere_api_key=COHERE_API_KEY, model="command")

# Step 8: Create prompt template
template = """
You are an AI assistant helping to summarize and analyze a text document.

Here is the document content:
{text}

📌 Summary:
- Provide a concise summary of the document.

📌 Key Takeaways:
- List 3 important points from the text.

📌 Sentiment Analysis:
- Determine if the sentiment of the document is Positive, Negative, or Neutral.
"""

prompt_template = PromptTemplate(input_variables=["text"], template=template)

# Step 9: Generate output only if text_content is loaded
if text_content:
    formatted_prompt = prompt_template.format(text=text_content)
    response = cohere_llm.predict(formatted_prompt)
    print("\n📌 *Formatted Output* 📌")
    print(response)
else:
    print("⚠ Skipping output generation due to missing file.")