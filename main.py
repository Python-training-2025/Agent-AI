
from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY")

model = OllamaModel(
    model_name="llama2:7b",
    base_url="http://localhost:11434/v1",
)

agent = Agent(model=model)
result = agent.run_sync("what is a fish?")
print(result.data)

