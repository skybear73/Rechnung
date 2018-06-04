
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# Assign spreadsheet filename to `file`
file = 'C:/Users/Michael/Desktop/Anlagenwerte/Anlagenauswertung_09_02/Auswertung_70%_eta4_etaX.xls'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Tabelle1')

df2 = xl.parse('Tabelle2')
print(df1)
print(df2)

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()