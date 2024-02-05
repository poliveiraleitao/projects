import tkinter
from tkinter import Canvas, PhotoImage  # Import Canvas and PhotoImage from tkinter module
import tkinter.simpledialog as simpledialog
import tkinter.ttk as ttk  # Import for styled dialog
import random
import pandas as pd
import os


# ---------------------------- CONSTANTS ----------------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
LANGUAGE = "Spanish"               # sets the initial language
WORD = 'None'                      # sets the initial word
CARD_IMAGE_FILE = 'card_front.png' # sets the initial card image
NUM_PLAYS = -1                     # start countdown for num_plays
SCORE = 0
ORIGINAL_SPANISH_WORD = None       # store the spanish word choosed by select_word => used in the change_language functions
CARD_IMAGE_FRONT_OR_BACK = None    # define variable for the card image

# ---------------------------- EXCEL DATA_BASE------------------------------------- #

def load_dataframe(filename):
    if os.path.exists(filename):
        return pd.read_excel(filename)
    else:
        print(f"File {filename} not found. Loading default file.")
        return pd.read_excel("espanhol-5k-palabras.xlsx")

# ---------------------------- GET PLAYERS NAME--------- ------------------------------- #

# Function to get the player's name using a popup window
def get_player_name():
    dialog = tkinter.Tk()  # Create a Tkinter window for the dialog
    prompt_label = ttk.Label(dialog, text="¿Cómo te llamas?", font=(FONT_NAME, 30), foreground="blue")
    prompt_label.pack(pady=100)

    player_name = simpledialog.askstring("¡Hola! ", "¿Cómo te llamas?", parent=dialog)  # Get player name

    dialog.destroy()  # Close the dialog window

    return player_name

# Function to determine the filename to load based on player's name
def determine_filename(player_name):
    if player_name:
        return f"{player_name}_espanhol-5k-palabras.xlsx"
    else:
        return "espanhol-5k-palabras.xlsx"


# Function to save the DataFrame to the specified filename
def save_dataframe(filename, dataframe):
    dataframe.to_excel(filename, index=False)
    print(f"DataFrame saved to {filename}")

def end_game():
    global DF, player_filename

    # Save the DataFrame to the appropriate filename
    save_dataframe(player_filename, DF)
    # Close the tkinter window
    window.destroy()

# ---------------------------- CHANGE SELECT WORD--------- ------------------------------- #

def select_word():
    global WORD, DF, NUM_PLAYS, SCORE, ORIGINAL_SPANISH_WORD  # calls global WORD variable

    NUM_PLAYS += 1                                                   # start counting the number of games
    window.title(f' Holla {player_name.upper()}, you have {SCORE} POINTS / {NUM_PLAYS} TRIES')

    #set the language title to spanish again
    LANGUAGE = "Spanish"
    canvas.itemconfig(language_title, text=LANGUAGE)

    change_background(LANGUAGE)  # Pass card_image_item_id

    #Filter out words that are already learned
    unknown_words = DF[DF['KNOWN'] == False]

    if unknown_words.shape[0] > 0:
        random_index = random.randint(0, unknown_words.shape[0] - 1)  # Generate a random index to select a row
        random_row = unknown_words.iloc[random_index]                    # Select a random row from the DataFrame

        # Extract the values from the random row
        WORD = random_row['SPANISH']                     # change displayed word
        canvas.itemconfig(word_title, text=WORD)         # Update the canvas with the new word

    else:
        # Handle scenario where all words are known
        print("Congratulations! You have learned all the words!")
        window.destroy()  # Close the window

    ORIGINAL_SPANISH_WORD = WORD

# ---------------------------- CHANGE LANGUAGE ------------------------------------ #
def change_language_english():
    global WORD, LANGUAGE, ORIGINAL_SPANISH_WORD

    # Find the English translation
    english_translation = DF[DF['SPANISH'] == ORIGINAL_SPANISH_WORD]['ENGLISH'].values[0]  #use ORIGINAL_SPANISH_WORD TO FIND TRANSLATION
    WORD = english_translation
    LANGUAGE = "English"

    canvas.itemconfig(word_title, text=WORD)  #change the language title
    canvas.itemconfig(language_title, text=LANGUAGE)  # change the language title

    change_background(LANGUAGE)  # Pass card_image_item_id

def change_language_portuguese():
    global WORD, LANGUAGE, ORIGINAL_SPANISH_WORD

    spanish_word = WORD

    # Find the Portuguese translation
    portuguese_translation = DF[DF['SPANISH'] == ORIGINAL_SPANISH_WORD]['PORTUGUESE'].values[0] #use ORIGINAL_SPANISH_WORD TO FIND TRANSLATION
    WORD = portuguese_translation
    LANGUAGE = "Português"

    canvas.itemconfig(word_title, text=WORD)  #change the language title
    canvas.itemconfig(language_title, text=LANGUAGE)  # change the language title

    change_background(LANGUAGE)  # Pass card_image_item_id
# ---------------------------- CHANGE BACK-GROUND -------------------------------- #
def change_background(LANGUAGE):
    global CARD_IMAGE_FRONT_OR_BACK, card_image, CARD_IMAGE_FILE

    if LANGUAGE == 'Spanish':
        # Update the card image path
        CARD_IMAGE_FILE = 'card_front.png'
    else:
        # Update the card image path
        CARD_IMAGE_FILE = 'card_back.png'

    # Create a new PhotoImage object with the updated card image
    card_image = PhotoImage(file=CARD_IMAGE_FILE)

    # Update the canvas item to display the new image
    canvas.itemconfig(CARD_IMAGE_FRONT_OR_BACK, image=card_image)

# ---------------------------- STORE UNKNOWN WORDS -------------------------------- #
# Function to mark a word as known
def mark_known():
    global WORD, DF, SCORE

    SCORE += 1

    # Mark the word as known in the DataFrame
    DF.loc[DF['SPANISH'] == WORD, 'KNOWN'] = True

    # Check if all words are known
    if not DF['KNOWN'].any():
        end_game()
    else:
        # Select a new random word
        select_word()


# ---------------------------- UI SETUP ------------------------------------------- #
window = tkinter.Tk()
window.title('Learn Spanish')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card Front image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = PhotoImage(file=CARD_IMAGE_FILE)
CARD_IMAGE_FRONT_OR_BACK = canvas.create_image(400, 263, image=card_image) #start with x and y coord
language_title = canvas.create_text(400, 150, text = LANGUAGE, fill='black', font=(FONT_NAME, 30, 'italic'))
word_title = canvas.create_text(400,270, text = WORD, fill='black', font=(FONT_NAME, 30, 'bold'))
canvas.grid(row=1, column=0, columnspan=2) #columnspan makes the image occupies 2 columns

# Button X
button_x_image = PhotoImage(file='wrong.png')
button = tkinter.Button(image=button_x_image, command=select_word, highlightthickness=0, borderwidth=0)
button.grid(row=2, column=0, padx=150, pady=5, sticky='w')

# Button V
button_v_image = PhotoImage(file='right.png')
button = tkinter.Button(image=button_v_image, command=mark_known, highlightthickness=0, borderwidth=0)
button.grid(row=2, column=1, padx=150, pady=5, sticky='w')

# Button English
button_english_image = PhotoImage(file='english.png')
button = tkinter.Button(image=button_english_image, command=change_language_english, highlightthickness=0, borderwidth=0, highlightbackground=BACKGROUND_COLOR )
button.grid(row=0, column=0, padx=150, pady=20, sticky='w')

# Button Portugues
button_portuguese_image = PhotoImage(file='portugues.png')
button = tkinter.Button(image=button_portuguese_image, command=change_language_portuguese, highlightthickness=0, borderwidth=0, highlightbackground=BACKGROUND_COLOR)
button.grid(row=0, column=1, padx=150, pady=20, sticky='w')

# Button End Game
button_end_game_image = PhotoImage(file='end_game.png')
button = tkinter.Button(image=button_end_game_image, command=end_game, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
button.grid(row=3, column=0, columnspan=2) #columnspan makes the image occupies 2 columns

# ---------------------------- START QUIZ ------------------------------------------- #

# Load player name
player_name = get_player_name()
player_filename = determine_filename(player_name)

# Load DataFrame from the appropriate Excel file
DF = load_dataframe(player_filename)

select_word()

window.mainloop()