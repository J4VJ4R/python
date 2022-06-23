import csv

with open('people.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print("Apellido paterno: {0}, Apellido Materno: {1}, Nombre: {2}, Ciudad. {3}".format(row[0], row[1], row[2], row[3]))