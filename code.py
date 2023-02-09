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

  

