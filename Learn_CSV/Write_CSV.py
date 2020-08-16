import csv

with open("testdata.csv", 'w', newline="") as f:
    write = csv.writer(f)
    heading = ['S.No', 'F_Name', "L_Name"]
    write.writerow(heading)

    data = [
            [1, 'G', 'J'],
            [2, 'B', 'M'],
            [3, 'B', 'M']
            ]

    write.writerows(data)