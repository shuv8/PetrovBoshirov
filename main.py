import pandas as pd
import numpy as np
import os
import glob
from transliterate import get_translit_function
import matplotlib.pyplot as plt

#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
#pd.set_option('display.max_colwidth', None)

def open_csv_file():
    csv_file = pd.read_csv('BoardingData.csv', delimiter=';')
    return csv_file

def open_tab_file():
    tab_file = pd.read_fwf('Sirena-export-fixed.tab')
    tab_file.rename(columns={'FlightCode': 'FlightNumber', 'TravelDoc': 'PassengerDocument'}, inplace=True)
    return tab_file

def open_xml_file():
    xml_file = pd.read_csv('PointzAggregator-AirlinesData.csv', delimiter=';')
    return xml_file

def open_yaml_file():
    yaml_file = pd.DataFrame()
    yaml_files_path = r'D:\Учеба\7 семестр\PetrovBoshirov\YamlToCsv'
    for file_name in glob.glob(os.path.join(yaml_files_path, '*.csv')):
        buf_yaml_file = pd.read_csv(file_name, delimiter=';')
        yaml_file = yaml_file.append(buf_yaml_file, sort=False)
    return yaml_file

def open_excel_file():
    excel_file = pd.DataFrame()
    excel_files_path = r'D:\Учеба\7 семестр\PetrovBoshirov\YourBoardingPassDotAero'
    for file_name in glob.glob(os.path.join(excel_files_path, '*.csv')):
        buf_excel_file = pd.read_csv(file_name, delimiter=';')
        excel_file = excel_file.append(buf_excel_file, sort=False)
    return excel_file

def open_json_file():
    flights_json = pd.read_csv('flights.csv', delimiter=',')
    loyalty_json = pd.read_csv('loyality.csv', delimiter=',')
    persons_json = pd.read_csv('persons.csv', delimiter=',')
    json_file = flights_json.merge(loyalty_json, how='inner', on='NickName')
    json_file = json_file.merge(persons_json, how='inner', on='NickName')
    json_file['Number'] = json_file['Number'].apply(str)
    json_file['Card number'] = json_file['Programm'].str.cat(json_file['Number'], sep=" ")
    json_file.rename(columns={'First_Name': 'First name', 'Last_Name': 'Second name', 'Flight': 'FlightNumber', 'Date': 'FlightDate'}, inplace=True)
    return json_file


csv_data = open_csv_file()
xml_data = open_xml_file()
#excel_data = open_excel_file()
#tab_data = open_tab_file()

csv_data.rename(columns={'PassengerFirstName': 'First name', 'PassengerLastName': 'Second name', 'PassengerSecondName': 'Middle name'}, inplace=True)
xml_data.rename(columns={'Code': 'FlightNumber', 'Date': 'FlightDate'}, inplace=True)

boarding_data_with_bonus = csv_data.merge(xml_data[['First name', 'Second name', 'Card number', 'FlightNumber', 'FlightDate']], on=['First name', 'Second name', 'FlightNumber', 'FlightDate'], how='left')
#boarding_data_with_bonus = boarding_data_with_bonus.merge(json_data[['NickName', 'First name', 'Second name', 'Card number', 'FlightNumber', 'FlightDate']], on=['First name', 'Second name', 'FlightNumber', 'FlightDate'], how='left')
#boarding_data_with_bonus = boarding_data_with_bonus.merge(json_data[['NickName', 'First name', 'Second name', 'Card number', 'FlightNumber', 'FlightDate']], on=['Card number', 'FlightNumber', 'FlightDate'], how='left')
#print(boarding_data_with_bonus['Card number'].isna().sum())
#print(boarding_data_with_bonus['NickName'].isna().sum())
#print(boarding_data_with_bonus.head(30))

#print(boarding_data_with_bonus['PassengerDocument'].unique())

unique_docs = boarding_data_with_bonus['PassengerDocument'].value_counts()
#print(unique_docs)
people_list = pd.DataFrame(columns=['First name', 'Second name', 'PassengerDocument', 'Number of flights', 'Number of bonus use', 'Percent of bonus use'])
people_list = people_list.astype({"Number of flights": "float", "Number of bonus use": "float", "Percent of bonus use": "float"})
#print(people_list.info())
pre_stats = unique_docs.describe()
unique_docs.plot(kind='hist')
plt.show()
print('####################################################################')
print(pre_stats)
print('####################################################################')
print(csv_data['Destination'].value_counts())
#i = 1
test_df = boarding_data_with_bonus.sample(frac=0.01)
#print(test_df.info())

for psg in boarding_data_with_bonus['PassengerDocument'].unique():
    if unique_docs[psg] > pre_stats.at['max'] * 0.75:
        buf_df = boarding_data_with_bonus[boarding_data_with_bonus['PassengerDocument'] == psg]
        cards = buf_df['Card number'].notna().sum()
        buf_df = buf_df.reset_index()
        new_row = {'First name': buf_df.at[0, 'First name'], 'Second name': buf_df.at[0, 'Second name'], 'PassengerDocument': psg, 'Number of flights': unique_docs[psg], 'Number of bonus use': cards, 'Percent of bonus use': cards/unique_docs[psg]}
        people_list = people_list.append(new_row, ignore_index=True)
        #print('---Done---', (i / len(boarding_data_with_bonus['PassengerDocument'].unique())) * 100, '%')
        #i += 1
    else:
        pass
print(people_list)
stats = people_list.describe()
print(stats)
bonus_stat = stats.at['25%', 'Percent of bonus use']
spies_list = people_list[people_list['Percent of bonus use'] <= bonus_stat]

csv_data = csv_data.loc[csv_data['PassengerDocument'].isin(spies_list['PassengerDocument'].tolist())]

print('####################################################################')
print(spies_list)
print('####################################################################')
for item in csv_data['PassengerBirthDate'].unique():
    print(item)

csv_data = csv_data.loc[~csv_data['PassengerDocument'].isin(['0931 650989', '6435 081994'])]
spies_list = spies_list.loc[~spies_list['PassengerDocument'].isin(['0931 650989', '6435 081994'])]

print('####################################################################')
print(spies_list)
spies_list = spies_list.reset_index()
# print(csv_data)
for i in spies_list['PassengerDocument'].tolist():
    karas = csv_data.loc[csv_data['PassengerDocument'] == i][['FlightDate', 'FlightNumber', 'Destination']]
    karas = karas.sort_values(by='FlightDate')
    print('################', spies_list.loc[spies_list['PassengerDocument'] == i]['Second name'].tolist()[0],'#################')
    print(karas)

print('####################################################################')
print(csv_data['Destination'].value_counts())
# text = 'ЛЮБОВЬ КОЧЕРГИНА'
# translit_ru = get_translit_function('ru')
# translit_ru(text, reversed=True)
#print(translit_ru(text, reversed=True))
