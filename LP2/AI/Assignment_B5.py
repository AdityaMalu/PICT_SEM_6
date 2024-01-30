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
            'how many assignments have been completed': 'I have completed 5 assignments.',
            'what is the name of the course': 'The name of the course is Laboratory Practice 2.',
            'what is the name of the teacher': 'The name of the teacher is Ms. U.S.Pawar.',
            'what is the name of the college': 'The name of the college is Pune Institute of Computer Technology.',
            'what is the name of the department': 'The name of the department is Computer Engineering.',
            'what is the name of the university': 'The name of the university is Savitribai Phule Pune University.',
            'what is the name of the city': 'The name of the city is Pune.',
            'what is the name of the state': 'The name of the state is Maharashtra.',
            'what is the name of the country': 'The name of the country is India.',
            'what is the name of the continent': 'The name of the continent is Asia.',
            'what is the name of the planet': 'The name of the planet is Earth.',
            'what is the name of the galaxy': 'The name of the galaxy is Milky Way.',
            'what is the name of the universe': 'The name of the universe is Universe.',
            
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
