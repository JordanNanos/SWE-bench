import os
from openai import OpenAI

# Load API key from environment variable
client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY")
)

response = client.responses.create(
  model="gpt-4o-mini",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text);
