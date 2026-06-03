while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi!👋")
    
    elif user == "how are you":
        print("Bot: I'm fine, thanks!💙🤝")

    elif user =="who are you":
        print("Bot: I'm a Bot🤖")
    
    elif user == "bye":
        print("Bot: Goodbye!👋")
        break
    
    else:
        print("Bot: I don't understand😕")