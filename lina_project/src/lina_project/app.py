from embedchain import App
from dotenv import load_dotenv
import os

load_dotenv()

# Välj mellan LM Studio eller Ollama
USE_LM_STUDIO = True  # Ändra till False för att använda Ollama

if USE_LM_STUDIO:
    # Konfiguration för LM Studio
    from embedchain.llm.openai import OpenAI
    
    llm = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        model="local-model",
        base_url="http://localhost:1234/v1"
    )
else:
    # Konfiguration för Ollama
    from embedchain.llm.ollama import Ollama
    llm = Ollama(model="mistral")

# Skapa appen med lokal embedding-modell
app = App(
    llm=llm,
    embedder="sentence-transformers/all-MiniLM-L6-v2"
)

# Lägg till data
app.add("data.txt")  # Skapa denna fil i samma mapp

# Kör chatten
while True:
    query = input("\nAnge din fråga (eller 'avsluta'): ")
    if query.lower() == "avsluta":
        break
    response = app.query(query)
    print(f"\nSvar: {response}")