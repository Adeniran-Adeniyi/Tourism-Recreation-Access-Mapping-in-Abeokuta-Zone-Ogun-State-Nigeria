import csv
#with open('Abk_zone.csv', encoding='utf-8-sig') as f:
#    reader = csv.DictReader(f)
 #   rows = list(reader)

#print("Number of rows:", len(rows))
#print("columes: ", list(rows[0].keys()))
#values = []
#for row in rows:
#    value = float(row['Area_km2'])
 #   values.append(value)   
  #  raw = row['Area_km2'].strip()
 #   if raw == "":
#        continue
#    values.append(float(raw))


#print("lergest value:", max(values))
#print("smallest value:", min(values))
#print("count:", len(values))

def inspect_data(filename, column):
    with open(filename, encoding = 'utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return{
        'smallest':min(values),
        'highest':max(values),
        'count':len(values)
    }

result = inspect_data('Abk_zone.csv','Area_km2')
print(result)
result = inspect_data('Abk_zone.csv','ward')
print(result)