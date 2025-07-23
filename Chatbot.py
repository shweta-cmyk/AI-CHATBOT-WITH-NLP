import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot, here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I am doing well, thank you for asking.",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"quit|bye|goodbye",
        ["Goodbye!", "Take care!", "Bye!"]
    ],
    [
        r"(.*) your purpose(.*)",
        ["My purpose is to answer your questions and assist you.",]
    ],
    [
        r"(.*) weather in (.*)",
        ["I'm sorry, I don't have access to real-time weather information.",]
    ],
    [
        r"(.*) help (.*)",
        ["I can try to help you with common questions and provide information.",]
    ],
    [
        r"(.*) (thank you|thanks)",
        ["You're welcome!", "No problem!", "Glad to help!"]
    ],
    [
        r"(.*)", # Default response
        ["I'm not sure how to respond to that.", "Can you please rephrase that?", "Could you tell me more?"]
    ]
]

# Initialize the chatbot
def chatbot():
    print("Hi, I am a chatbot. Let's chat!")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    # Download necessary NLTK data (if not already downloaded)
    try:
        nltk.data.find('corpora/wordnet')
    except:
        nltk.download('wordnet')
    try:
        nltk.data.find('tokenizers/punkt')
    except:
        nltk.download('punkt')

    chatbot()
