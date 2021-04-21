import Project_Weekly_Billing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import unittest


class Check_Weekly_Billing(unittest.TestCase):

    def __init__(self):
        self.project_details = Project_Weekly_Billing.pyTips.df
        self.unique_employee = self.project_details.User.unique()
        self.unique_tags = self.project_details.Tag.unique()
        self.result_billing_amt_in_USR = self.project_details['Billing Amount in USD'].sum(
        )
        self.result_billing_amt_in_INR = self.project_details['Billing Amount in INR'].sum(
        )
        self.result_total_hrs_spent = self.project_details['Hours(For Calculation)'].sum(
        )

    def test_check_parameter(self):

        self.assertEqual(
            self.unique_employee, Project_Weekly_Billing.pyTips.employee)
        self.assertEqual(self.unique_tags, Project_Weekly_Billing.pyTips.tags)
        self.assertEqual(self.result_billing_amt_in_USR,
                         Project_Weekly_Billing.pyTips.billing_amt_in_USR)
        self.assertEqual(self.result_billing_amt_in_INR,
                         Project_Weekly_Billing.pyTips.billing_amt_in_INR)
        self.assertEqual(self.result_total_hrs_spent,
                         Project_Weekly_Billing.pyTips.total_hrs_spent)

    def test_calculate_activity_summary(self):
        result_calculate_activity_summary = pd.pivot_table(self.project_details, index=[
                                                           'Tag'], columns='User', values="Hours(For Calculation)", aggfunc=np.sum)
        self.assertEqual(result_calculate_activity_summary,
                         Project_Weekly_Billing.pyTips.calculate_activity_summary())

    def test_calculate_employee_summary(self):
        result_calculate_employee_summary = self.project_details.groupby(
            'User').agg({'Hours(For Calculation)': 'sum'})
        self.assertEqual(result_calculate_employee_summary,
                         Project_Weekly_Billing.pyTips.calculate_employee_summary())


if __name__ == '__main__':
    unittest.main()
