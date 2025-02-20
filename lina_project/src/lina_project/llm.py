from crewai import LLM

# Konfiguration för att ansluta CrewAI till LM Studio
llm = LLM(
    model="ollama/llama-3-8b-instruct",  # Se till att modellen finns i LM Studio
    base_url="http://127.0.0.1:1234/v1",  # LM Studio's lokala API-server
    api_key="sk-no-key-required",  # LM Studio kräver ingen riktig API-nyckel
    temperature=0.7,
    timeout=120,
    max_tokens=4000,
    top_p=0.9,
    frequency_penalty=0.1,
    presence_penalty=0.1,
    response_format={"type": "json"},
    seed=42
)

print("CrewAI är kopplad till LM Studio!")