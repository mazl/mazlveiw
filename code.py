import csv
file=csv.DictReader(open("./data.csv"))
with open('./res.csv','w') as csvfile:
    header=['country','year','cases']
    writer=csv.writer(csvfile)
    writer.writerow(header)
    for line in file:
        data=list(line.items())
        for i in data[1:]:
            writer.writerow(list(data[0][1:]+i))

with open('./res.csv', 'r', newline='') as f_input:
    csv_input = csv.DictReader(f_input)
    data = sorted(csv_input, key=lambda row: (row['year']))

with open('./output.csv', 'w', newline='') as f_output:    
    csv_output = csv.DictWriter(f_output, fieldnames=csv_input.fieldnames)
    csv_output.writeheader()
    csv_output.writerows(data)

