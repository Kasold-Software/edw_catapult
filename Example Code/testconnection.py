import pyodbc
import pandas as pd
print('test')
conn = pyodbc.connect(driver='{SQL Server}', server='ALPHA', trusted_connection='yes')
print('test')

#cursor = cnxn.cursor()