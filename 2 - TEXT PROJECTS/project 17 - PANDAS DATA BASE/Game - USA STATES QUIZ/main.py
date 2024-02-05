import turtle
import pandas
import time

#read data with pandas
DB_NAME = '50_states.csv'
data = pandas.read_csv(DB_NAME)

#-----------------------------------------------------------

# Create a dictionary to store state coordinates
state_coordinates = {}

#-----------------------------------------------------------

# Populate the dictionary with state coordinates
def create_dictionary():
    for index, row in data.iterrows():
        states = row['state'].lower()
        x = int(row['x'])
        y = int(row['y'])
        state_coordinates[states] = (x, y)

#ask for a state name
def ask_state_name():
    user_input = screen.textinput(title=f'{score}/50 states correct', prompt='Whats another states name?')
    return user_input.lower()

# Check if the entered state name is in the dictionary
def get_correct_state_name(user_input):
    global score  # Global variable to keep track of the score
    if user_input in state_coordinates and user_input not in correctly_guessed_states:
        #add guessed state to the set of correctly guessed states
        correctly_guessed_states.add(user_input)

        score +=1 #increment the score
        screen.title('U.S. States Game | Time to complete 8:00') # Update the screen title with the score

        #get coordinates of state
        x, y = state_coordinates[user_input]

        #call function to write state name
        write_state_name(user_input, x, y)

    elif user_input in correctly_guessed_states:
        print("you've already guessed this state!")
    else:
        print("State not found.")

# Draw the state name at the corresponding coordinates
def write_state_name(state_name, x, y):
    t = turtle.Turtle()
    t.penup()
    t.goto(x, y)
    t.write(user_input, align="center", font=("Arial", 12, "normal"))
    t.hideturtle()

def start_timer(duration):
    print("Timer started. You have 8 minutes to guess all states.")
    start_time = time.time()
    time_limit = 8 * 60 #minutes in seconds
    return start_time, time_limit

# Function to display 3 initial letters of a random state
#def display_help():
    # Select a random state from the list
#    random_state = random.choice(states)

    # Display 3 initial letters of the random state
#    help_text = random_state[:3]
#    turtle.clear()  # Clear the previous help text, if any
#    turtle.write(f"Help: {help_text}", align="center", font=("Arial", 16, "normal"))

#create csv with all states that were not guessed
def states_to_learn(all_states, guessed_states):
    #get list
    list_states_to_learn = [state for state in all_states if state not in correctly_guessed_states]
        #states_to_learn = all_states - guessed_states
        #list_states_to_learn = all_states - correctly_guessed_states
    print(list_states_to_learn)

    # save the result as csv
    df = pandas.DataFrame({'States to Learn': list(list_states_to_learn)})
    df.to_csv('states_to_learn.csv', index=False)

#-----------------------------------------------------------

#starting the game
create_dictionary() #store name of the states in the BD_NAME database
score = 0 #keep track of the score
correctly_guessed_states = set() # Create a set to keep track of correctly guessed states

#setup screen
screen = turtle.Screen()
screen.title('U.S. States Game | Time to complete 8:00')
screen.setup(height=500, width=735)

image = 'blank_states_img.gif' #load the image that will be used as screen
screen.addshape(image) #add image as the turtle shape
turtle.shape(image) #use image as turtle shape

#-----------------------------------------------------------

# Start the timer and give 8 minutes to complete
start_time, time_limit = start_timer(8)

#check if user guessed all states
while True:  # Check if 8 minutes have elapsed
    elapsed_time = time.time() - start_time
    if elapsed_time >= time_limit:
        turtle.clear()
        turtle.write("Time is up!", align="center", font=("Arial", 16, "normal"))
        states_to_learn(set(state_coordinates.keys()), correctly_guessed_states)
        break

    else:
        # Check if the user has guessed all states
        if len(correctly_guessed_states) == 50:
            turtle.write("Congratulations! You won!!", align="center", font=("Arial", 16, "normal"))
            break

        user_input = ask_state_name()
        if user_input is None:  # If the user closes the input window
            states_to_learn(set(state_coordinates.keys()), correctly_guessed_states)
            break
        elif user_input.lower() == 'exit':
            states_to_learn(set(state_coordinates.keys()), correctly_guessed_states)
            break
        else:
            get_correct_state_name(user_input)











