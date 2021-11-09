import openpyxl
import csv
import os
import glob

field_names = ['Sequence', 'Mrs/Ms', 'Name', 'Class', 'FlightNumber', 'DepartureCity', 'DepartureAirport', 'ArrivalCity', 'ArrivalAirport', 'Date', 'Time', 'Airline', 'Seat', 'PNR', 'E-ticket', 'BonusCard']

def excel_to_csv(excel_file):
    wb = openpyxl.load_workbook(excel_file)

    csv_file_name = excel_file.replace('.xlsx', '.csv')
    your_csv_file = open(csv_file_name, 'w')
    wr = csv.DictWriter(your_csv_file, fieldnames=field_names, delimiter=';')
    wr.writeheader()

    for sheet_name in wb.sheetnames:
        sh = wb[sheet_name]
        wr.writerow({'Sequence': sh['H1'].value, 'Mrs/Ms': sh['A3'].value, 'Name': sh['B3'].value, 'Class': sh['H3'].value, 'FlightNumber': sh['A5'].value, 'DepartureCity': sh['D5'].value, 'DepartureAirport': sh['D7'].value, 'ArrivalCity': sh['H5'].value, 'ArrivalAirport': sh['H7'].value, 'Date': sh['A9'].value, 'Time': sh['C9'].value, 'Airline': sh['E9'].value, 'Seat': sh['H11'].value, 'PNR': sh['B13'].value, 'E-ticket': sh['E13'].value, 'BonusCard': sh['F3'].value})

    your_csv_file.close()

excel_files_path = 'C:\\Users\\plomb\\PycharmProjects\\pandas0\\YourBoardingPassDotAero'

#i = 1
for file_name in glob.glob(os.path.join(excel_files_path, '*.xlsx')):
    #print(fileName, '---Done---', (i/366)*100, '%')
    #i += 1
    excel_to_csv(file_name)
