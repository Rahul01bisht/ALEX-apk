import webbrowser

def multi_search(user_input):
    user_input = user_input.lower()

    if "youtube" in user_input:
        query = user_input.replace("youtube", "").strip()
        print ("Searching . . . .")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

    elif "google" in user_input:
        query = user_input.replace("google", "").strip()
        print ("Searching . . . .")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "instagram" in user_input or "insta" in user_input:
        query = user_input.replace("instagram", "").replace("insta", "").strip()
        print ("Searching . . . .")
        webbrowser.open(f"https://www.instagram.com/explore/tags/{query}/")

    elif "spotify" in user_input:
        query = user_input.replace("spotify", "").strip()
        print ("Searching . . . .")
        webbrowser.open(f"https://open.spotify.com/search/{query}")

    else:
        print("Sorry, I can't search that yet.")
        
if __name__ == ("__main__"):        

    while True:
        user_input = input("You: ")

        if "stop" in user_input:
            print("Okay, goodbye!")
            break

        multi_search(user_input)            