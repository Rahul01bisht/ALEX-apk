
def load_brain(file_path):
    brain = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if "::" in line:
                question, answer = line.strip().split("::", 1)
                brain[question.lower()] = answer
    return brain

def query_brain(brain, user_input):
    user_input = user_input.lower()
    return brain.get(user_input, "Sorry, I don't understand that yet.")
    
if __name__ == ("__main__"):
    
    brain = load_brain("brain.txt")    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "stop":
            print("Alex: Goodbye!")
            break
        print("Alex:", query_brain(brain, user_input))


# Example usage
#