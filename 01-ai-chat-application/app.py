from openai_client import client
from config import MODEL

user_prompt = input("Enter your prompt: ")

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a Senior DevOps Engineer."},
        {"role": "user", "content": user_prompt}
    ]
)

print("\nAI:")
print(response.choices[0].message.content)