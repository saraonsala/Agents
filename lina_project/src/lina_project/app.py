from embedchain import App
from dotenv import load_dotenv
import os

load_dotenv()

# Välj mellan LM Studio eller Ollama
USE_LM_STUDIO = True  # Ändra till False för att använda Ollama

if USE_LM_STUDIO:
    # Korrigerad import för nyare version av Embedchain
    from embedchain.llm.openai import OpenAILlm
    
    llm = OpenAILlm(
        api_key=os.getenv("OPENAI_API_KEY"),
        model="local-model",
        base_url="http://localhost:1234/v1"
    )
else:
    from embedchain.llm.ollama import Ollama
    llm = Ollama(model="mistral")

# Resten av koden förblir samma
app = App(
    llm=llm,
    embedder="sentence-transformers/all-MiniLM-L6-v2"
)

app.add("data.txt")

while True:
    query = input("\nAnge din fråga (eller 'avsluta'): ")
    if query.lower() == "avsluta":
        break
    response = app.query(query)
    print(f"\nSvar: {response}")