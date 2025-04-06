from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Error: GOOGLE_API_KEY environment variable is not set.")

# Initialize the Google Generative AI model with additional parameters
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # The specific model to use (e.g., "gemini-1.5-flash")
    temperature=0.7,          # Controls the randomness of the output (higher = more creative, lower = more deterministic)
    max_output_tokens=256,    # The maximum number of tokens (words or parts of words) in the output
    top_p=0.9,                # Nucleus sampling: considers the smallest set of tokens with a cumulative probability >= top_p
    top_k=40,                 # Limits the sampling pool to the top_k most likely tokens
    api_key=api_key           # The API key for authentication with the Google Generative AI service
)

# Layman explanation:
# - "model" is like choosing a specific brain for the AI.
# - "temperature" adjusts how creative or predictable the AI's responses are.
# - "max_output_tokens" limits how long the AI's response can be.
# - "top_p" ensures the AI picks from the most meaningful words.
# - "top_k" narrows down the AI's word choices to the top 40 most likely ones.

# Generate a response from the Google Generative AI model
# The `invoke` method sends a prompt to the model and gets a response.
# In this case, the prompt is "Hello, from Google Generative AI!".
response = llm.invoke("Hello, How are your, please Introduce yourself!")
print(response)  # Print the response from the model

