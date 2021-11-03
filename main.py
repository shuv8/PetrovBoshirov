import pandas as pd
import numpy as np

csvFile = pd.read_csv('BoardingData.csv', delimiter=';')
tabFile = pd.read_fwf('Sirena-export-fixed.tab')
csvFileInfo = csvFile.info()
tabFileInfo = tabFile.info()

#print(csvFileInfo)