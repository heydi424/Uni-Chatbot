import os
from openai import OpenAI

# 1. Create a client using the API key from the environment
def get_client():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set in the environment.")
    return OpenAI(api_key=api_key)

def chat():
    client = get_client()

    print("Chatbot (LLM, lightweight): Hi! Type 'bye' to exit.\n")

    # Keep a simple chat history so the model has context
    messages = [
        {"role": "system", "content": "You are a friendly, concise assistant."}
    ]

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Bot: Goodbye! 👋")
            break

        messages.append({"role": "user", "content": user_input})

        # 2. Call a lightweight model: gpt-4.1-mini
        response = client.chat.completions.create(
            model="gpt-4.1-mini",   # lightweight, fast model
            messages=messages,
        )

        bot_reply = response.choices[0].message.content
        print(f"Bot: {bot_reply}\n")

        messages.append({"role": "assistant", "content": bot_reply})

if __name__ == "__main__":
    chat()
