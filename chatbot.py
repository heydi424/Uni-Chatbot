from openai import OpenAI

client = OpenAI()

def chat():
    print("Uni (type 'exit' to quit)")
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant named Heydi."}
    ]

    while True:
        user_input = input("You: ")

        if user_input.strip().lower() == "exit":
            print("Heydi: Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages,
        )

        reply = response.choices[0].message.content
        print("Heydi:", reply)

        messages.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    chat()
