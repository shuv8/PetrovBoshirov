import xml.etree.ElementTree as ET
import csv

xml_file_path = 'PointzAggregator-AirlinesData.xml'
csv_file_path = xml_file_path.replace('.xml', '.csv')
field_names=['uid', 'First name', 'Second name', 'Card number', 'Bonus programm', 'Activity type', 'Code', 'Date', 'Departure', 'Arrival', 'Fare']

root_node = ET.parse('PointzAggregator-AirlinesData.xml').getroot()

# data = []
# i = 0

your_csv_file = open(csv_file_path, 'w')
wr = csv.DictWriter(your_csv_file, fieldnames=field_names, delimiter=';')
wr.writeheader()

for user_tag in root_node.findall('user'):
    # data.append(dict())
    # userid = usertag.get('uid')
    # data[i]['uid'] = userid
    # data[i]['First name'] = usertag.find('name').get('first')
    # data[i]['Second name'] = usertag.find('name').get('last')
    # data[i]['Cards'] = []
    # j = 0

    userid = user_tag.get('uid')
    f_name = user_tag.find('name').get('first')
    s_name = user_tag.find('name').get('last')
    for card_tag in user_tag.findall('cards/card'):
        # data[i]['Cards'].append(dict())
        # data[i]['Cards'][j]['Card number'] = cardtag.get('number')
        # data[i]['Cards'][j]['Bonus programm'] = cardtag.find('bonusprogramm').text
        # data[i]['Cards'][j]['Activities'] = []
        # k = 0

        card_n = card_tag.get('number')
        b_prog = card_tag.find('bonusprogramm').text
        for activity_tag in card_tag.findall('activities/activity'):
            # data[i]['Cards'][j]['Activities'].append(dict())
            # data[i]['Cards'][j]['Activities'][k]['Activity type'] = activitytag.get('type')
            # data[i]['Cards'][j]['Activities'][k]['Code'] = activitytag.find('Code').text
            # data[i]['Cards'][j]['Activities'][k]['Date'] = activitytag.find('Date').text
            # data[i]['Cards'][j]['Activities'][k]['Departure'] = activitytag.find('Departure').text
            # data[i]['Cards'][j]['Activities'][k]['Arrival'] = activitytag.find('Arrival').text
            # data[i]['Cards'][j]['Activities'][k]['Fare'] = activitytag.find('Fare').text
            # k += 1

            wr.writerow({'uid': userid, 'First name': f_name, 'Second name': s_name, 'Card number': card_n, 'Bonus programm': b_prog, 'Activity type': activity_tag.get('type'), 'Code': activity_tag.find('Code').text, 'Date': activity_tag.find('Date').text, 'Departure': activity_tag.find('Departure').text, 'Arrival': activity_tag.find('Arrival').text, 'Fare': activity_tag.find('Fare').text})
        # j += 1

    # i += 1

your_csv_file.close()
