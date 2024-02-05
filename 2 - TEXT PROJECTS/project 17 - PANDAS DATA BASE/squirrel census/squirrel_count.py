import pandas
DB_NAME = '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'

#read data with pandas
data = pandas.read_csv(DB_NAME)

#count occurrences of each color
color_counts = data['Primary Fur Color'].value_counts()

# Print the counts
print("Count of each primary fur color:")
print(color_counts)

#save the result as csv
DF = pandas.DataFrame(color_counts)
DF.to_csv('color_count.csv')