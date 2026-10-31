import csv 
def read_row(filename):
    with open(filename, encoding='utf-8-sig') as f:
        return(list(csv.DictReader(f)))





def clean_values(rows, column):
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return(values)

def summarise(values):
    if len(values) == 0:
        return{
            'count':0,
            'smallest':None,
            'largest':None,
            'Average':None
        }
    return{
        'smallest':min(values),
        'largest':max(values),
        'count':len(values),
        'average':sum(values) / len(values)
    }


rows = read_row('Abk_zone.csv')
values = clean_values(rows,'Area_km2')
summary = summarise(values)
print(summary)

def summarise_all(filename, columns):
    rows = read_row(filename)
    report = {}
    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarise(values)
    return report
report = summarise_all('Abk_zone.csv', ['Area_km2','ward'])
for column, stats in report.items():
    print(column, "->", stats)
