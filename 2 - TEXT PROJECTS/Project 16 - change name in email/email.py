
#file names
EMAIL_TEXT = 'text.txt'
NAMES_TEXT = 'names.txt'

def read_names():
    try:
        with open(NAMES_TEXT, 'r') as file:
            #read content
            content = file.read()

            #split content in a list of names (each name in a new line)
            NAMES = content.split('\n')

        return NAMES

    except FileNotFoundError:
        print(f"The file {NAMES_TEXT} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return[]

def write_email():
    try:
        #get names from the read_names function
        NAMES = read_names()

        with open(EMAIL_TEXT, 'r') as file:
            #read content
            content = file.read()

            #substitute [name]
            for name in NAMES:
                name_to_insert = name
                modified_content = content.replace("[name]", name_to_insert)
                save_new_email(name_to_insert, modified_content)

    except FileNotFoundError:
        print(f"The file {EMAIL_TEXT} was not found.")
        return[]
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def save_new_email(file_name, modified_content):
    new_email_file_name = f"new_{file_name}_email.txt"
    with open(new_email_file_name, 'w') as new_file:
        #write data to new file
        new_file.write(modified_content)
        print(f"New email saved as {new_email_file_name}")

write_email()