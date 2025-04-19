from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

# Import your AI functionalities
from Bakend.online import open_website
from Bakend.brain import load_brain, query_brain
from Bakend.search_engine import multi_search
from Bakend import __init__

class AlexApp(App):
    def build(self):
        self.brain = load_brain("Bakend/brain.txt")

        # Create the layout
        layout = BoxLayout(orientation='vertical')
        
        # Create a label
        self.label = Label(text="Hello, I am Alex. How can I help you?", size_hint=(1, 0.1))
        layout.add_widget(self.label)
        
        # Create a text input field
        self.text_input = TextInput(hint_text="Type something...", size_hint=(1, 0.2))
        layout.add_widget(self.text_input)
        
        # Create a button
        self.button = Button(text="Send", size_hint=(1, 0.2))
        self.button.bind(on_press=self.on_button_press)
        layout.add_widget(self.button)
        
        return layout
    
    def on_button_press(self, instance):
        # Get user input and provide response from the AI
        user_input = self.text_input.text.lower()
        
        if "stop" in user_input:
            self.label.text = "Okay, see you later!"
        elif any(site in user_input for site in ["youtube", "google", "insta", "instagram", "spotify"]):
            multi_search(user_input)
            self.label.text = "Opening your requested site."
        elif "open" in user_input:
            open_website()
            self.label.text = "Opening website."
        else:
            self.label.text = query_brain(self.brain, user_input)

# Run the app
if __name__ == '__main__':
    AlexApp().run()
    