def chatbot():
    print("🤖 Simple Chatbot - chatbot.py:2")
    print("Type 'bye' to exit\n - chatbot.py:3")

    while True:
        user = input("You: ").lower()

        if user == "hi":
            print("Bot: Hi! - chatbot.py:9")
        elif user == "how are you":
            print("Bot: I'm fine, thanks! - chatbot.py:11")
        elif user == "what is your name":
            print("Bot: I'm a simple Python chatbot. - chatbot.py:13")
        elif user == "who created you":
            print("Bot: Yukesh created me using Python! - chatbot.py:15")
        elif user == "bye":
            print("Bot: Goodbye! - chatbot.py:17")
            break
        else:
            print("Bot: Sorry, I don't understand that. - chatbot.py:20")


chatbot()
