class Chatbot:
    def __init__(self):
        self.responses = {
            'HELLO!': 'Hi Sayan! How can I assist you today?',
            'HOW ARE YOU?': 'I am just a chatbot, but I am doing great! How about you?',
            'WHAT IS YOUR NAME?': 'I am a chatbot created to assist you.',
            'WHAT IS YOUR INVENTION DAY?': 'My creation date is 03/08/2024.',
            'BYE FRIEND': 'Goodbye! Have a great day!',
        }
    
    def get_response(self, user_input):
        user_input = user_input.upper()
        # Direct matching rather than regex
        return self.responses.get(user_input, "I'm sorry, I don't understand that.")

def main():
    print("Chatbot: Type 'Bye' to end the conversation.")
    chatbot = Chatbot()
    
    while True:
        user_input = input("You: ")
        if user_input.strip().upper() == 'BYE':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()