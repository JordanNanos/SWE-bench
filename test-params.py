import os
from openai import OpenAI

# Load API key from environment variable
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# Test different parameter combinations to find what's causing the 400 error
model = "gpt-5-nano-2025-08-07"
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello"}
]

test_cases = [
    {"temperature": 1.0},  # Only temperature
    {"temperature": 1.0, "top_p": 0.95},  # Temperature + top_p
    {"temperature": 1.0, "top_p": 1.0},   # Temperature + top_p=1.0
    {"top_p": 0.95},  # Only top_p
    {},  # No extra parameters
]

for i, params in enumerate(test_cases):
    print(f"\nTest {i+1}: {params}")
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            **params
        )
        print("✓ Success!")
    except Exception as e:
        print(f"✗ Error: {e}")
