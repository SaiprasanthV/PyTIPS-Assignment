import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Project():
    def __init__(self, df):
        self.df = df
        self.employee = df.User.unique()
        self.tags = df.Tag.unique()
        self.billing_amt_in_USR = df['Billing Amount in USD'].sum()
        self.billing_amt_in_INR = df['Billing Amount in INR'].sum()
        self.total_hrs_spent = df['Hours(For Calculation)'].sum()

    def calculate_activity_summary(self):
        return(pd.pivot_table(df, index=['Tag'], columns='User', values="Hours(For Calculation)", aggfunc=np.sum))

    def calculate_employee_summary(self):
        return(df.groupby('User').agg({'Hours(For Calculation)': 'sum'}))

    def display_bar_chart(self):
        barG = df.groupby('User').agg({'Billing Amount in INR': 'sum'})
        return(barG.plot(kind='bar', cmap='Accent'))


df = pd.read_csv("timesheet.csv")

df = df.dropna(how='all', axis='rows')
df = df.dropna(how='all', axis='columns')
df = df[:223]

df['Billing Amount in USD'] = np.where(df['Role'].str == 'Employee', 25, 40)

df['Billing Amount in INR'] = df['Billing Amount in USD']*74.53

df['Hours(For Calculation)'] = pd.to_numeric(df['Hours(For Calculation)'])

print(df)

pyTips = Project(df)
print('Employees:', pyTips.employee)
print('Tags:', pyTips.tags)
print('Billing Amount in USR:', pyTips.billing_amt_in_USR)
print('Billing Amount i INR:', pyTips.billing_amt_in_INR)
print(pyTips.total_hrs_spent)
print(pyTips.calculate_activity_summary())
print(pyTips.calculate_employee_summary())
# print(pyTips.)
pyTips.display_bar_chart()
plt.show()
