import pandas as pd

#read data with panda
data = pd.read_csv('weather_data.csv')
print(data)

#define name of new file
NEW_FILE = 'new_file_pandas.txt'

def write_new_file():
    with open(NEW_FILE, 'w') as file:
        #iterate over the data
        for index, row in data.iterrows():
            day = row['day']
            temp = int(row['temp'])
            condition = row['condition']
            temp_suffix = "degrees" if temp != 1 else "degree"

            # Write information to the file
            file.write(f'On {day}, the temperature was {temp} {temp_suffix} and it was {condition.lower()}.\n')

    print(f"The weather report has been saved to {NEW_FILE}.")

def average_temp():
    print(data['temp'].mean())
    print(data['temp'].max())


# Call the function to write the new file
write_new_file()
average_temp()
print(data['day'] == 'Monday')

# Find the row number where the day is 'Monday'
monday_row_number = data[data['day'] == 'Monday'].index[0] + 1  # Adding 1 to start counting from 1 instead of 0

print("Row number where the day is Monday:", monday_row_number)