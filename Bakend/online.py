import webbrowser 
    
def open_website():    
    while True:
        user_input=input("You : ").lower()
        
        if "youtube" in user_input: 
            print("Opening . . . .")
            print("Opening YouTube.")
            webbrowser.open("https://youtube.com")
            
        elif "google" in user_input:
            print("Opening . . . .")
            print("Opening Google.") 
            webbrowser.open("https://google.com")
            
        elif "insta"  in user_input:
             print("Opening . . . .")
             webbrowser.open("https://www.instagram.com")
             
        elif "spotify"  in user_input:
             print("Opening . . . .")
             webbrowser.open("https://open.spotify.com")
             
        elif "stop" in user_input:
            print ("Okay, stopping web search.")
            return 
            
if __name__ == ("__main__"):
    open_website()        