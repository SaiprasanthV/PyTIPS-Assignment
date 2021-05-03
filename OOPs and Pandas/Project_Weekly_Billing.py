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
        return(barG.plot(kind='bar', cmap='Accent', rot=10,  figsize=(13, 7), title='Employee vs Billing', fontsize=10))


class Employee():
    def __init__(self, df):
        '''
        arg -> dataframe (df)
        task -> calculates multiple summary reports
        '''
        self.df = df
        self.projects = df['Project Name'].unique()
        self.tags = df.Tag.unique()
        self.billing_amt_in_USR = df['Billing Amount in USD'].sum()
        self.billing_amt_in_INR = df['Billing Amount in INR'].sum()
        self.total_hrs_spent = df['Hours(For Calculation)'].sum()

    def calculate_activity_summary(self):
        return(pd.pivot_table(df, index=['Tag'], columns='Project Name', values="Hours(For Calculation)", aggfunc=np.sum))

    def calculate_project_summary(self):
        return(df.groupby('Project Name').agg({'Hours(For Calculation)': 'sum'}))

    def display_bar_chart(self):
        barG = df.groupby('Project Name').agg({'Billing Amount in INR': 'sum'})
        return(barG.plot(kind='bar', cmap='Accent', rot=0, figsize=(13, 7), title='Project vs Billing', fontsize=10))


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


def project_or_employee_selection():
    print(''' What do you want to look ? -  Projects / Employees
          Type '1' for "Projects",
          Type '2' for "Employees"
          Type 'q' to Quit''')
    class_selected = input()
    if (class_selected == '1' or class_selected == '2'):
        return(class_selected)

    elif (class_selected == 'q'):
        print('System is going to Exit !!')
        exit()

    else:
        print('Enter a Valid number!!')
        return(project_or_employee_selection())


def project_name():
    print('Kindly Enter the name of the project you want to know!')
    project_names = df["Project Name"].unique()
    print(project_names, sep="\n")
    print('Note: Type "q" to quit')
    project_name_x = input()

    if project_name_x in project_names:
        return(project_name_x)

    elif (project_name_x == 'q'):
        print('System is going to Exit !!')
        exit()

    else:
        print('Enter Valid Project Name:')
        return(project_name())


def employee_name():
    print('Kindly Enter the name of the Employee you want to know!')
    employee_names = df["User"].unique()
    print(employee_names, sep="\n")
    print('Note: Type "q" to quit')
    employee_name_x = input()

    if employee_name_x in employee_names:
        return(employee_name_x)

    elif (employee_name_x == 'q'):
        print('System is going to Exit !!')
        exit()

    else:
        print('Enter Valid Employee Name:')
        return(employee_name())


if __name__ == '__main__':

    project_or_employee = project_or_employee_selection()
    if (project_or_employee == '1'):
        project = project_name()
        df = df.loc[df["Project Name"] == project]
        py_Project = Project(df)
        print('Employees:', py_Project.employee)
        print('Tags:', py_Project.tags)
        print('Billing Amount in USR: $', py_Project.billing_amt_in_USR)
        print('Billing Amount in INR: Rs.', py_Project.billing_amt_in_INR)
        print('Total hours spent:', py_Project.total_hrs_spent, 'hrs')
        print('Calculate activity summary (Tag vs Employee):\n',
              py_Project.calculate_activity_summary())
        print('Calculate Employee summary (Employee vs Hours spent):\n',
              py_Project.calculate_employee_summary())
        print('Employee vs Billing (Bar Graph):')
        py_Project.display_bar_chart()
        # plt.figure(figsize=(cm_to_inch(25), cm_to_inch(15)))
        plt.show()

    elif (project_or_employee == '2'):
        employee = employee_name()
        df = df.loc[df["User"] == employee]
        py_Employee = Employee(df)
        print('Employees:', py_Employee.projects)
        print('Tags:', py_Employee.tags)
        print('Billing Amount in USR: $', py_Employee.billing_amt_in_USR)
        print('Billing Amount in INR: Rs.', py_Employee.billing_amt_in_INR)
        print('Total hours spent:', py_Employee.total_hrs_spent, 'hrs')
        print('Calculate activity summary (Tag vs Employee):\n',
              py_Employee.calculate_activity_summary())
        print('Calculate Employee summary (Employee vs Hours spent):\n',
              py_Employee.calculate_project_summary())
        print('Employee vs Billing (Bar Graph):')
        py_Employee.display_bar_chart()
        plt.show()
