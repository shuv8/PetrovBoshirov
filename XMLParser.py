import xml.etree.ElementTree as ET
import csv

XMLFilePath = 'PointzAggregator-AirlinesData.xml'
CSVFilePath = XMLFilePath.replace('.xml', '.csv')
fieldNames=['uid', 'First name', 'Second name', 'Card number', 'Bonus programm', 'Activity type', 'Code', 'Date', 'Departure', 'Arrival', 'Fare']

root_node = ET.parse('PointzAggregator-AirlinesData.xml').getroot()

# data = []
# i = 0

your_csv_file = open(CSVFilePath, 'w')
wr = csv.DictWriter(your_csv_file, fieldnames=fieldNames, delimiter=';')
wr.writeheader()

for usertag in root_node.findall('user'):
    # data.append(dict())
    # userid = usertag.get('uid')
    # data[i]['uid'] = userid
    # data[i]['First name'] = usertag.find('name').get('first')
    # data[i]['Second name'] = usertag.find('name').get('last')
    # data[i]['Cards'] = []
    # j = 0

    userid = usertag.get('uid')
    FName = usertag.find('name').get('first')
    SName = usertag.find('name').get('last')
    for cardtag in usertag.findall('cards/card'):
        # data[i]['Cards'].append(dict())
        # data[i]['Cards'][j]['Card number'] = cardtag.get('number')
        # data[i]['Cards'][j]['Bonus programm'] = cardtag.find('bonusprogramm').text
        # data[i]['Cards'][j]['Activities'] = []
        # k = 0

        CardN = cardtag.get('number')
        BProg = cardtag.find('bonusprogramm').text
        for activitytag in cardtag.findall('activities/activity'):
            # data[i]['Cards'][j]['Activities'].append(dict())
            # data[i]['Cards'][j]['Activities'][k]['Activity type'] = activitytag.get('type')
            # data[i]['Cards'][j]['Activities'][k]['Code'] = activitytag.find('Code').text
            # data[i]['Cards'][j]['Activities'][k]['Date'] = activitytag.find('Date').text
            # data[i]['Cards'][j]['Activities'][k]['Departure'] = activitytag.find('Departure').text
            # data[i]['Cards'][j]['Activities'][k]['Arrival'] = activitytag.find('Arrival').text
            # data[i]['Cards'][j]['Activities'][k]['Fare'] = activitytag.find('Fare').text
            # k += 1

            wr.writerow({'uid': userid, 'First name': FName, 'Second name': SName, 'Card number': CardN, 'Bonus programm': BProg, 'Activity type': activitytag.get('type'), 'Code': activitytag.find('Code').text, 'Date': activitytag.find('Date').text, 'Departure': activitytag.find('Departure').text, 'Arrival': activitytag.find('Arrival').text, 'Fare': activitytag.find('Fare').text})
        # j += 1

    # i += 1

your_csv_file.close()
