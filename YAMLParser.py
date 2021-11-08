import csv
import yaml

YAMLFilePath = 'SkyTeam-Exchange.yaml'

fieldNames=['Date', 'Flight', 'Departure', 'Arrival', 'Status', 'Bonus card', 'Class', 'Fare']

with open(YAMLFilePath, 'r') as YAMLFile:
    YAMLData = yaml.safe_load(YAMLFile)

#i = 1
for day in YAMLData.keys():
    newname = day + '.csv'
    CSVFilePath = 'YamlToCsv/' + YAMLFilePath.replace('.yaml', newname)
    your_csv_file = open(CSVFilePath, 'w')
    wr = csv.DictWriter(your_csv_file, fieldnames=fieldNames, delimiter=';')
    wr.writeheader()
    for flight in YAMLData[day].keys():
        for card in YAMLData[day][flight]['FF'].keys():
            wr.writerow({'Date': day, 'Flight': flight, 'Departure': YAMLData[day][flight]['FROM'], 'Arrival': YAMLData[day][flight]['TO'], 'Status': YAMLData[day][flight]['STATUS'], 'Bonus card': card, 'Class': YAMLData[day][flight]['FF'][card]['CLASS'], 'Fare': YAMLData[day][flight]['FF'][card]['FARE']})
    your_csv_file.close()
    # print('---Done---', (i/365)*100, '%')
    # i += 1