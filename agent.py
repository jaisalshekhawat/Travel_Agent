from agent_history import State
from agent_summary import summarize_conversation
from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_version=os.getenv("AZURE_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY")
)
deployment = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")

state = State()

print("👋 Hello! I am your Travel Agent. Type 'exit' anytime to end the chat.\n")

# Ask initial questions first (once)
destination = input("Where are you traveling? ")
trip_type = input("What type of trip is it? (leisure, adventure, cultural) ")
days = input("How many days will your trip last? ")

state.add_message("user", f"I am going to {destination} for a {trip_type} trip lasting {days} days.")

response = client.chat.completions.create(
    model=deployment,
    messages=state.get_messages(),
    max_tokens=800,
    temperature=1.0,
)

reply = response.choices[0].message.content
state.add_message("assistant", reply)
print(f"\nAgent: {reply}\n")

# 🔄 Continuous chat loop
while True:
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Agent: Safe travels! 👋")
        break

    # Add user message to state
    state.add_message("user", user_input)

    # Generate assistant response
    response = client.chat.completions.create(
        model=deployment,
        messages=state.get_messages(),
        max_tokens=800,
        temperature=1.0,
    )

    reply = response.choices[0].message.content
    state.add_message("assistant", reply)

    print(f"\nAgent: {reply}\n")

    # Optionally update conversation summary
    summarize_conversation(state, client)
