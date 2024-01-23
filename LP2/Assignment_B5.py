import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            'hello': 'Hi there! How can I help you today?',
            'how are you': 'I am just a computer program, but I am doing well. How about you?',
            'i am fine': 'Great to hear that!',
            'what is your name': 'My name is Simple Chatbot.',
            'who are you': 'I am a Simple Chatbot.',
            'bye': 'Goodbye! If you have any more questions, feel free to ask.',
            'How many assignment have been completed': 'I have completed 5 assignments.',
            'What is the name of the course': 'The name of the course is Labrotary Practice 2.',
            
        }

        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()

    def preprocess_input(self, text):
        tokens = word_tokenize(text.lower())
        tokens = [self.stemmer.stem(token) for token in tokens if token.isalnum() and token not in self.stop_words]
        return tokens

    def respond(self, user_input):
        user_tokens = self.preprocess_input(user_input)

        for keyword in self.responses:
            if keyword in user_tokens:
                return self.responses[keyword]

        return "I'm sorry, I didn't understand that. Can you please rephrase your question?"

def main():
    chatbot = SimpleChatbot()
    print("Hello! I'm a simple chatbot. You can start the conversation or type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break

        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
