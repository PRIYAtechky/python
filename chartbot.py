import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses using pattern-response pairs
pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you", ["I'm just a chatbot.", "I'm doing fine, thanks!"]],
    ["what's your name", ["I'm a chatbot.", "I don't have a name."]],
    ["bye|goodbye", ["Goodbye!", "See you later!", "Bye!"]],
]

# Create a chatbot using the defined patterns and responses
chatbot = Chat(pairs, reflections)

# Chat loop
def chat_loop():
    print("Chatbot: Hi! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    nltk.download("punkt")
    chat_loop()
