import tkinter as tk
from random import choice
from dataWork import UseData
import random
# Sample words and mnemonics
words = [
    {"word": "Bonjour", "meaning": "Hello (French)", "mnemonic": "Bon = Good, Jour = Day"},
    {"word": "Hola", "meaning": "Hello (Spanish)", "mnemonic": "Sounds like Holla!"},
    # Add more words here

    # word # meaning # mnemonic
]

german_txt = "german_verb.csv"

class FlashcardApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Vocabulary Flashcards")
        self.german = UseData.read_in_german(german_txt)
        
        #####3 ONLY FOR TESTING
        self.chooseLanguage( 0)
        print ("Dict size")
        # change this later in the choose language func
        self.len_dict = len(self.dict)

        # inital page to 0 where u choose the language
        # page useful for knowing which row im on in my list of dict
        # starts from -1 because page will be first  and i call nextword() even for the first word
        self.page = -1
        # What is this doing
        self.word_label =tk.Label(
            root,
            text="Hello, Tkinter!", 
            font=("Helvetica", 24, "bold"),  # Font family, size, and weight
            fg="#ffffff",  # Text color
            bg="#3498db",  # Background color
            padx=20,  # Padding around text horizontally
            pady=20,  # Padding around text vertically
            relief="flat",  # Adds a 3D effect (flat, raised, sunken, ridge, etc.)
            borderwidth=5,  # Border thickness
        )
        self.word_label.pack(pady=20)
        
        self.mnemonic_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.mnemonic_label.pack(pady=10)

        # Set up buttons
        self.show_mnemonic_button = tk.Button(root, text="Show Meaning", command=self.show_meaning)
        self.show_mnemonic_button.pack(pady=10)

        self.next_word_button = tk.Button(root, text="Next Word", command=self.next_word)
        self.next_word_button.pack(pady=10)

        self.random_word_button = tk.Button(root, text="Random Word", command=self.random_word)
        self.random_word_button.pack(pady=10)

        # Display the first word in order
        # self.next_word()
        # Display random word
        self.random_word()
        print("am i here")

    # implement the function that would choose the language
    def chooseLanguage(self, num):
        if num == 0:
            self.dict = UseData.read_in_german(german_txt)
        
        self.txtfile = german_txt
        return 0
    
    ##
    # this function take the next chronological word
    # i call this also for the first word thats why self.page strats at -1
    def next_word(self):
        # block or pop up (need to add) if no more rows
        if (self.page +1 < self.len_dict):
            # increment the page as we are taking new word
            self.page +=1
            self.current_word = self.dict[self.page]['word']
            #self.current_word = choice(words)
            
            # update the word
            self.word_label.config(text=self.current_word)

            # remove the mnemonic 
            self.mnemonic_label.config(text="")
            
            # reset the button text from hide -> show
            self.show_mnemonic_button.config(text="Show Meaning")

    def random_word(self):
        random_w = random.randint(0, self.len_dict-1)
        self.page = random_w
        self.current_word = self.dict[self.page]['word']
        self.word_label.config(text=self.current_word)

            # remove the mnemonic 
        self.mnemonic_label.config(text="")
            
            # reset the button text from hide -> show
        self.show_mnemonic_button.config(text="Show Meaning")
    
    # button to submit the input for mnemonic
    def submit(self):
        # Get the input from the Entry widget
        input_text = self.input_field.get()
        print(input_text)

        # row is page +1  since csv has a header,
        #  txtfile initalized in chooselanguage
        UseData.update_in_german(self.txtfile, self.page+1, input_text)

    ### Function called when button show meaning is pressed, make the meaning appear
    def show_meaning(self):
        # self.mnemonic_label.config(text=f"{self.current_word['meaning']}\nMnemonic: {self.current_word['mnemonic']}")
        meaning = self.german[self.page]['meaning']
        mnemonic = self.german[self.page]['mnemonic']
        self.mnemonic_label.config(text=f"{meaning}\nMnemonic: {mnemonic}")
        self.show_mnemonic_button.config(text="Hide Meaning", command=self.hide_meaning)

        ## If no mnemonic then create and save
        # if (self.dict[self.page]['mnemonic']==""):
        #     self.input_field = tk.Entry(root, width=30)
        #     self.input_field.pack(pady=10)
        #     submit_button = tk.Button(root, text="Submit", command=self.submit)
        #     submit_button.pack(pady=10)

    def hide_meaning(self):
        self.mnemonic_label.config(text="")
        self.show_mnemonic_button.config(text="Show Meaning", command=self.show_meaning)

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.geometry("400x600+50+100")
    root.mainloop()