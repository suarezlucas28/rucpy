from models import Ruc
import csv
i = 0

with open('/home/luke/workspace/rucpy/rucs/csv/ruc', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        i += 1
        ruc = Ruc()
        ruc.ci = row[0]
        ruc.name = row[1]
        ruc.dv = row[2]
        ruc.save()

