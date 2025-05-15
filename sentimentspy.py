# Program to check the sentiment of a sentence
import colorama
import emoji
from colorama import Fore, Style
from textblob import TextBlob

#initializes colorama for colored output
colorama.init()

#start printing emojis for the program
print(f"{FORE.CYAN} ???????? Welcome to Sentiment Spy: ????{STYLE.RESET_ALL}")

username=input(f"{FORE.MAGENTA} Please enter your name: {Style.RESET_ALL}").strip()
if not username:
    username= "Mystery Agent"
conversation_history = []
print(f"{FORE.CYAN} Hello! Agent {username}")    
print("Type a sentence so that I can analyse the sentiment using TextBlob")
print(f"Type{Fore.YELLOW} reset {Fore.CYAN} , exit to quit or history")
while True:
    user_input = input().srtip()
    if not user_input:
        print("Please enter a text or some valid command.")
        continue
    else :
        if user_input.lower() == "exit":
            print(f" Exiting Sentiment Spy. Goodbye {username}")
            break
        elif user_input.lower() == "reset":
            conversation_history.clear
            print("All conversation history cleared!")
            continue
        elif user_input.lower() == "history":
            if not conversation_history:
                print("No conversations yet!")
            else:
                print("Conversation History\n")    
                for idx,(text,polarity, sentiment_type) in enumerate(conversation_history,start =1):
                    if sentiment_type == "Positive":
                        color = Fore.GREEN
                        emoji = ":grinning_face:"
                    elif sentiment_type == "Negative" :
                        color   = Fore.RED
                        emoji = ":sad_face:"
                    else:
                        color = Fore.YELLOW
                        emoji = ":neutral_face:"

                    print(f"{idx}.{color}{emoji}{text}" f"{polarity:.2f},{sentiment_type}){Style.RESET_ALL}")
    continue      

# Sentiment Analysis
polarity = TextBlob(user_input).sentiment.polarity
if polarity > 0.25:
    sentiment_type = "Positive"
    color = Fore.GREEN
    emoji = ":grinning_face:"
elif polarity < -0.25:
    sentiment_type = "Negative"    
    color = Fore.RED
    emoji = ":sad_face:"
else:
    sentiment_type = "Neutral"    
    color =Fore.YELLOW
    emoji = ":neutral_face:"

conversation_history.append(user_input, polarity, sentiment_type)    
print(f"{color}{emoji}{sentiment_type} sentiment detected with polarity {polarity}")
