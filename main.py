import pandas as pd
import numpy as np
import os
import glob


def open_files():
    csv_file = pd.read_csv('BoardingData.csv', delimiter=';')
    tab_file = pd.read_fwf('Sirena-export-fixed.tab')
    xml_file = pd.read_csv('PointzAggregator-AirlinesData.csv', delimiter=';')
    yaml_file = pd.DataFrame()
    yaml_files_path = r'D:\Учеба\7 семестр\PetrovBoshirov\YamlToCsv'
    for file_name in glob.glob(os.path.join(yaml_files_path, '*.csv')):
        buf_yaml_file = pd.read_csv(file_name, delimiter=';')
        yaml_file = yaml_file.append(buf_yaml_file, sort=False)
    excel_file = pd.DataFrame()
    excel_files_path = r'D:\Учеба\7 семестр\PetrovBoshirov\YourBoardingPassDotAero'
    for file_name in glob.glob(os.path.join(excel_files_path, '*.csv')):
        buf_excel_file = pd.read_csv(file_name, delimiter=';')
        excel_file = excel_file.append(buf_excel_file, sort=False)
    flights_json = pd.read_csv('flights.csv', delimiter=',')
    loyalty_json = pd.read_csv('loyality.csv', delimiter=',')
    persons_json = pd.read_csv('persons.csv', delimiter=',')
    json_file = flights_json.merge(loyalty_json, how='inner', on='NickName')
    json_file = json_file.merge(persons_json, how='inner', on='NickName')
    return csv_file, tab_file, xml_file, yaml_file, excel_file, json_file

# csvFileInfo = csv_file.info()
# tabFileInfo = tabFile.info()


csv_data, tab_data, xml_data, yaml_data, excel_data, json_data = open_files()

print(json_data.info())
print(json_data)