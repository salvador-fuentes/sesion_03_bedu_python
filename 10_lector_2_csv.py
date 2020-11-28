##Una segunda manera de leer archivos csv. Las filas se convierten en diccionarios. 

import csv

filename = 'employees.csv'

with open(filename, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # print(row['Salary'])
        s = row.get('Salary')
        n = row.get('Name')
        print(f'{n} earns {s}')
