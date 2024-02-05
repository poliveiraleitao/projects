import csv

#file names
WEATHER_DATA = 'weather_data.csv'
NEW_FILE = 'new_file.txt'

#create empty list to store the data
days = []
temperatures = []
conditions = []

#read the data from the csv file
def read_data():
    try:
        with open(WEATHER_DATA, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row

            # Iterate over each row in the CSV file
            for row in csv_reader:
                # Extract data from each row
                day = row[0]
                temperature = int(row[1])  # Convert temperature to integer
                condition = row[2]

                # Append data to the respective lists
                days.append(day)
                temperatures.append(temperature)
                conditions.append(condition)

    except FileNotFoundError:
        print(f"The file {WEATHER_DATA} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return[]

def write_new_file():
    with open(NEW_FILE, 'w') as file:
        #iterate over the data
        for day, temp, condition in zip(days, temperatures, conditions):
            temp_suffix = "degrees" if temp != 1 else "degree"

            #write info on file
            file.write(f'On {day}, the temperature was {temp} {temp_suffix} and it was {condition.lower()}.\n')

    print(f"The weather report has been saved to {NEW_FILE}.")

# Call the functions
read_data()
write_new_file()