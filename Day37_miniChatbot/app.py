def chatbot():
    print("Hello! I'm your mini chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            response = generate_response(user_input)
            print(f"Chatbot: {response}")
            
def generate_response(user_input):
    # Simple response generation logic
    if "hello" in user_input.lower():
        return "Hello! How can I help you?"
    elif "how are you" in user_input.lower():
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "what is your name" in user_input.lower():
        return "I'm your friendly mini chatbot!"
    else:
        return "I'm not sure how to respond to that. Can you ask something else?"


if __name__ == "__main__":
    chatbot()