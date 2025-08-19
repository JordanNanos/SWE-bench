import os
from openai import OpenAI

# Load API key from environment variable
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# Test 1: List available models
print("Available models:")
try:
    models = client.models.list()
    for model in models.data:
        if "gpt" in model.id.lower():
            print(f"  {model.id}")
except Exception as e:
    print(f"Error listing models: {e}")

print("\n" + "="*50 + "\n")

# Test 2: Try the specific model with minimal request
print("Testing gpt-5-nano-2025-08-07:")
try:
    response = client.chat.completions.create(
        model="gpt-5-nano-2025-08-07",
        messages=[
            {"role": "user", "content": "Hello"}
        ],
        temperature=1.0  # Use the default temperature
    )
    print("Success! Model works.")
    print(f"Response: {response.choices[0].message.content}")
except Exception as e:
    print(f"Error with gpt-5-nano-2025-08-07: {e}")

print("\n" + "="*50 + "\n")

# Test 3: Try a known working model for comparison
print("Testing gpt-4o-mini for comparison:")
try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "Hello"}
        ],
        temperature=0.7
    )
    print("Success! gpt-4o-mini works.")
    print(f"Response: {response.choices[0].message.content}")
except Exception as e:
    print(f"Error with gpt-4o-mini: {e}")
