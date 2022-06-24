import csv
from tkinter import W

people = [
    ['Palacios', 'Rivas', 'Adan', 'CDMX'],
    ['Torres', 'Palacios', 'Sandra', 'MOSQUERA'],
    ['Martinez', 'Martinez', 'Jose', 'TIJUANA'],
]

with open('people.csv', 'w', newline='') as filecsv:
    writer = csv.writer(filecsv, delimiter=' ')
    writer.writerows(people)