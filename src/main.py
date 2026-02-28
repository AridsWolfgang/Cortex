from chatbot import MultidisciplinaryChatbot

def main():
    bot = MultidisciplinaryChatbot()
    print("Welcome to Cortex! Ask questions across math, economics, business, finance, programming, history, art, or electrical engineering. Type 'exit' to quit.")
    while True:
        query = input("\nYour query: ")
        if query.lower() == 'exit':
            break
        response = bot.process_query(query)
        print("\nCortex response:\n" + response)

if __name__ == "__main__":
    main()