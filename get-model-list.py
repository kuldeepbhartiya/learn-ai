import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key =  os.getenv("GOOGLE_API_KEY")
print(f"API Key loaded from environment: '{api_key}'")

# Configure the Generative AI SDK with your API key
if api_key:
    genai.configure(api_key=api_key)
else:
    print("Error: GOOGLE_API_KEY not found in environment variables. "
          "Please ensure you have set it up correctly.")
    exit()

def list_available_models():
    """Lists the names of the generative models available through the Gemini API
    that support the 'generateContent' method.
    """
    try:
        print("Available Gemini models that support 'generateContent':")
        for model in genai.list_models():
            if "generateContent" in model.supported_generation_methods:
                print(f"- {model.name}")
    except Exception as e:
        print(f"An error occurred while listing models: {e}")
        print("Please ensure your API key is valid and properly configured.")

if __name__ == "__main__":
    list_available_models()