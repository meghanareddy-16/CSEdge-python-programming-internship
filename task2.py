import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Define patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I assist you today?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you! How can I assist you?",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created to help you. You can call me Chatbot.",]
    ],
    [
        r"can you help me with (.*)",
        ["Sure, I can help you with %1. Please provide more details.",]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem! Happy to help."]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day!", "Bye! Take care!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that. Can you rephrase?"]
    ],
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Function to run the chatbot
def chatbot_conversation():
    print("Hi, I am a simple chatbot. You can start chatting with me (type 'quit' to stop).")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

# Run the chatbot conversation
if __name__ == "__main__":
    chatbot_conversation()
