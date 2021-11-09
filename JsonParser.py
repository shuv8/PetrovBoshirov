import pandas as pd
import json
import numpy as np


#jsonFile = pd.read_json(r'C:\Users\stari\Desktop\Универ\Дата\Airlines-All\Airlines\FrequentFlyerForum-Profiles.json')
#print(jsonFile)
#jsonFileInfo = jsonFile.info()
#print(jsonFile)
#print(data[1])


with open('FrequentFlyerForum-Profiles.json') as frequent_flyer_forum_profiles_data:
    data = json.load(frequent_flyer_forum_profiles_data)

field_names_flights = ['NickName', 'Date', 'Codeshare', 'Dep_city', 'Dep_airport', 'Dep_country',
              'Flight', 'Arrival_city', 'Arrival_airport', 'Arrival_county']
field_value_flights = []
field_names_loyality = ['NickName', 'Status', 'Programm', 'Number']
field_value_loyality = []
field_names_persons = ['NickName', 'Sex', 'Last_Name', 'First_Name']
field_value_persons = []

for index1 in data["Forum Profiles"]:
    for index2 in index1["Registered Flights"]:
        temp = [index1["NickName"]]
        temp.append(index2["Date"])
        temp.append(index2["Codeshare"])
        temp.append(index2["Departure"]["City"])
        temp.append(index2["Departure"]["Airport"])
        temp.append(index2["Departure"]["Country"])
        temp.append(index2["Flight"])
        temp.append(index2["Arrival"]["City"])
        temp.append(index2["Arrival"]["Airport"])
        temp.append(index2["Arrival"]["Country"])

        field_value_flights.append(temp)

    for index3 in index1["Loyality Programm"]:
        temp = [index1["NickName"]]
        temp.append(index3["Status"])
        temp.append(index3["programm"])
        temp.append(index3["Number"])

        field_value_loyality.append(temp)

        temp = [index1["NickName"], index1["Sex"]]
        temp.append(index1["Real Name"]["Last Name"])
        temp.append(index1["Real Name"]["First Name"])

        field_value_persons.append(temp)

data_frame_flights = pd.DataFrame(field_value_flights, columns=field_names_flights)
data_frame_loyality = pd.DataFrame(field_value_loyality, columns=field_names_loyality)
data_frame_persons = pd.DataFrame(field_value_persons, columns=field_names_persons)

data_frame_flights.to_csv(r'flights.csv', index_label='id')
data_frame_loyality.to_csv(r'loyality.csv', index_label='id')
data_frame_persons.to_csv(r'persons.csv', index_label='id')

# print(field_value_flights[0])
# print(field_value_loyality[0])
# print(field_value_persons[0])


#print(data["Forum Profiles"][0]["Registered Flights"][0])


#print(data)