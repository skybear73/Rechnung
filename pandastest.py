import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plt.style.use('ggplot')

# Assign spreadsheet filename to `file`
file = 'C:/Users/Michael/Desktop/Anlagenwerte/Anlagenauswertung_09_02/Auswertung_70%_eta4_etaX.xls'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Tabelle1')
#print(df1)
df2 = xl.parse('Tabelle2')
#print(df2)

#print(df1.describe())


ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
#ts.plot()

df = pd.DataFrame(df1, index=df1.index, columns=["Zeit [s] - Plot 0", "Leistung P [W] - P-V", "Wirkungsgrad eta [%] - eta-V"])
df.plot(x="Zeit [s] - Plot 0", y="Leistung P [W] - P-V", y="Wirkungsgrad eta [%] - eta-V")
#df.plot()
#df = df.cumsum()
#print(df)
#plt.figure(); df.plot(); plt.legend(loc='best')
plt.show()
plt.close()