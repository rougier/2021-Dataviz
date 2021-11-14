import os
import csv
from dbfpy import dbf

path = "/Users/rougier/tmp/dataviz"

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('.DBF'):
            csv_fn = filename[:-4]+ ".csv"
            with open(csv_fn,'wb') as csvfile:
                in_db = dbf.Dbf(os.path.join(dirpath, filename))
                out_csv = csv.writer(csvfile)
                names = []
                for field in in_db.header.fields:
                    names.append(field.name)
                out_csv.writerow(names)
                for rec in in_db:
                    out_csv.writerow(rec.fieldData)
                in_db.close()
