import groq
import os
import time

# API key
client = groq.Groq(api_key="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")  

# Welcome message
print("🤖 Welcome to thy Royal AI Chatbot! Type 'exit' to take thy leave.\n")

# Ask for name
user_name = input("Pray, noble traveler, what be thy name? ")
print(f"\n👑 Greetings, {user_name} of the realm! How may I be of service?\n")

# System prompt
system_prompt = {
    "role": "system",
    "content": "You are the royal advisor to Queen Elizabeth I, answering all questions in noble Old English with utmost respect and dramatic flourish, as if thou wert writing a letter to the court."
}

# Start chat loop
while True:
    user_input = input(f"{user_name}: ")
    if user_input.lower() == 'exit':
        print("🪶 Fare thee well, noble soul!")
        break

    # Send only current message along with system prompt
    messages = [
        system_prompt,
        {"role": "user", "content": user_input}
    ]

    # Get response from Groq
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=messages
    )

    # Extract and display response
    reply = response.choices[0].message.content

    # Typing effect (for realism)
    print("AI 🤖: ", end="", flush=True)
    for char in reply:
        print(char, end="", flush=True)
        time.sleep(0.015)
    print("\n")
