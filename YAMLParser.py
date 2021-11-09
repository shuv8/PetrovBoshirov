import csv
import yaml

yaml_file_path = 'SkyTeam-Exchange.yaml'

field_names=['Date', 'Flight', 'Departure', 'Arrival', 'Status', 'Bonus card', 'Class', 'Fare']

with open(yaml_file_path, 'r') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

#i = 1
for day in yaml_data.keys():
    new_name = day + '.csv'
    csv_file_path = 'YamlToCsv/' + yaml_file_path.replace('.yaml', new_name)
    your_csv_file = open(csv_file_path, 'w')
    wr = csv.DictWriter(your_csv_file, fieldnames=field_names, delimiter=';')
    wr.writeheader()
    for flight in yaml_data[day].keys():
        for card in yaml_data[day][flight]['FF'].keys():
            wr.writerow({'Date': day, 'Flight': flight, 'Departure': yaml_data[day][flight]['FROM'], 'Arrival': yaml_data[day][flight]['TO'], 'Status': yaml_data[day][flight]['STATUS'], 'Bonus card': card, 'Class': yaml_data[day][flight]['FF'][card]['CLASS'], 'Fare': yaml_data[day][flight]['FF'][card]['FARE']})
    your_csv_file.close()
    # print('---Done---', (i/365)*100, '%')
    # i += 1