import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Project():
    def __init__(self, df):
        '''
        arg -> dataframe (df)
        task -> calculates multiple summary reports
        '''
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


# reading csv file
df = pd.read_csv(r"OOPs and Pandas\timesheet.csv")
# df = pd.read_csv("timesheet.csv")

# creating a constant for USR to INR conversion
INR_USR_constant = 74.53

# removing the rows and columns in which all values are filled with 'None'
df = df.dropna(how='all', axis='rows')
df = df.dropna(how='all', axis='columns')

# removing the last two lines which has the total summary of the sheet
df = df[:223]

# creating column for 'Billing Amount in USD' and entering value as 25 for Employee and 40 for other
df['Billing Amount in USD'] = np.where(df['Role'].str == 'Employee', 25, 40)

# creating column for 'Billing Amount in INR' and entering respective Billing value in INR
df['Billing Amount in INR'] = df['Billing Amount in USD']*INR_USR_constant

# converting the valuue of 'Hours(For Calculation)' from String to Float
df['Hours(For Calculation)'] = pd.to_numeric(df['Hours(For Calculation)'])

print(df)

pyTips = Project(df)
print('Employees:', pyTips.employee)
print('Tags:', pyTips.tags)
print('Billing Amount in USR:', pyTips.billing_amt_in_USR)
print('Billing Amount i INR:', pyTips.billing_amt_in_INR)
print('Total hours spent:', pyTips.total_hrs_spent)
print('Calculate activity summary (Tag vs Employee):\n',
      pyTips.calculate_activity_summary())
print('Calculate Employee summary (Employee vs Hours spent):\n',
      pyTips.calculate_employee_summary())
print('Employee vs Billing (Bar Graph):')
pyTips.display_bar_chart()
plt.show()
