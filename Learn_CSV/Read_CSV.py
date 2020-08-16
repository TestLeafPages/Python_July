# for read
import csv


# with open("animal.csv") as f:
#     reader = csv.reader(f)          # Single di []
#     # for row in reader:
#     #     for cell in row:
#     #         print(cell)
#
#     for row in reader:
#         print(row[0].ljust(10), row[1].ljust(10), row[2].ljust(10), row[3].ljust(10), row[4])


with open("animal.csv") as f:
    reader = csv.DictReader(f)      # multi di [k][v]
    for i in reader:
       print(i['s.no'].ljust(5), i['animal'].ljust(10), i['age'].ljust(5), i['visits'])