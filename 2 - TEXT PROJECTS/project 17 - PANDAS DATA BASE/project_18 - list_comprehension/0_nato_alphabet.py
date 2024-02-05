# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

#read data with pandas
NATO_ALPHABET = 'nato_phonetic_alphabet.csv'
data = pandas.read_csv(NATO_ALPHABET)

#-----------------------------------------------------------

# Create a dictionary with the letter and the nato code
nato_alphabet_dict = {}

#-----------------------------------------------------------

# Populate the dictionary
def create_nato_dictionary():
    for index, row in data.iterrows():
        letter = row['letter'].upper()
        code = row['code']
        #insert rows in the nato_alphabet_dict
        nato_alphabet_dict[letter] = code

#get each letter in the word
def get_letter_from_word():
    word = input('Insert word: ').upper()
    letter_list = [letter for letter in word]
    return letter_list

#assign nato code to each letter
def assing_nato_code(letters):
    # new_dict = {new_key:new_value for (key, value) in dict.items() if test}
    letter_nato_code = {letter: nato_alphabet_dict[letter] for letter in letters if letter in nato_alphabet_dict}
    print(letter_nato_code)

#____________________________________________________________
# Main function to run the program
def main():
    create_nato_dictionary()
    letters = get_letter_from_word()
    assing_nato_code(letters)

if __name__ == "__main__":
    main()

