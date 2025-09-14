import os

def summarize_conversation(state, client):
    """
    Summarizes the conversation using the provided Azure OpenAI client.
    """
    deployment = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")  # ✅ load deployment here

    summary_prompt = (
        f"Current summary: {state.summary}\nUpdate it based on new messages."
        if state.summary
        else "Create a summary of the conversation above."
    )

    messages = state.get_messages() + [{"role": "user", "content": summary_prompt}]

    response = client.chat.completions.create(
        model=deployment,   
        messages=messages,
        max_tokens=500,    
        temperature=0.7,    
    
    )
    
    state.summary = response.choices[0].message.content.strip()
    return state.summary
