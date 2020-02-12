# Basic visualization of data set - most popular male surnames in Poland (2020-01-22)
# csv file access - 2020-02-12
# https://dane.gov.pl/dataset/568,nazwiska-wystepujace-w-rejestrze-pesel/resource/21713/table

import csv
import matplotlib.pyplot as plt

"""Generate the chart for male surnames"""
with open('data/SurnamesMale.csv', encoding='utf8') as file:
    reader = csv.reader(file)

    # Read/skip the header row
    header = next(reader)

    # Header not read from the file - translation to English hardcoded
    header = ['Surname', 'Occurences']

    surnames = []
    occurences = []
    count = 0
    for row in reader:
        count += 1
        surname = row[0]
        surnames.append(surname)
        occurences_nr = int(row[1])
        occurences.append(occurences_nr)
        # read 10 first rows
        if count == 10:
            break

# plot the bar char
plt.title('The most popular male surnames in Poland')
plt.ylabel('Number of male people with a given surname')
plt.bar(surnames, occurences)
plt.show()
