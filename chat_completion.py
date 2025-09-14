import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_version=os.getenv("AZURE_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY")  
)

deployment=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")

destination = input("Where are you going?")

response = client.chat.completions.create(
    model=deployment,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": f"I am going to {destination}, what should I see?",
        }
    ],
    max_tokens=4096,
    temperature=1.0,
    top_p=1.0
)

print(response.choices[0].message.content)
