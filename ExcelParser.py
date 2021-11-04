import openpyxl
import csv
import os
import glob

fieldNames = ['Sequence', 'Mrs/Ms', 'Name', 'Class', 'FlightNumber', 'DepartureCity', 'DepartureAirport', 'ArrivalCity', 'ArrivalAirport', 'Date', 'Time', 'Airline', 'Seat', 'PNR', 'E-ticket', 'BonusCard']

def excel_to_csv(excelFile):
    wb = openpyxl.load_workbook(excelFile)

    csvFileName = excelFile.replace('.xlsx', '.csv')
    your_csv_file = open(csvFileName, 'w')
    wr = csv.DictWriter(your_csv_file, fieldnames=fieldNames, delimiter=';')
    wr.writeheader()

    for sheetName in wb.sheetnames:
        sh = wb[sheetName]
        wr.writerow({'Sequence': sh['H1'].value, 'Mrs/Ms': sh['A3'].value, 'Name': sh['B3'].value, 'Class': sh['H3'].value, 'FlightNumber': sh['A5'].value, 'DepartureCity': sh['D5'].value, 'DepartureAirport': sh['D7'].value, 'ArrivalCity': sh['H5'].value, 'ArrivalAirport': sh['H7'].value, 'Date': sh['A9'].value, 'Time': sh['C9'].value, 'Airline': sh['E9'].value, 'Seat': sh['H11'].value, 'PNR': sh['B13'].value, 'E-ticket': sh['E13'].value, 'BonusCard': sh['F3'].value})

    your_csv_file.close()

excelFilesPath = 'C:\\Users\\plomb\\PycharmProjects\\pandas0\\YourBoardingPassDotAero'

#i = 1
for fileName in glob.glob(os.path.join(excelFilesPath, '*.xlsx')):
    #print(fileName, '---Done---', (i/366)*100, '%')
    #i += 1
    excel_to_csv(fileName)
