from Project_Weekly_Billing import Project, pyTips
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import unittest
from pandas.testing import assert_series_equal
from pandas.testing import assert_frame_equal


class test_Weekly_Billing(unittest.TestCase):

    def setUp(self):
        self.project_details = pyTips.df
        self.unique_employee = self.project_details.User.unique()
        self.unique_tags = self.project_details.Tag.unique()
        self.result_billing_amt_in_USR = self.project_details['Billing Amount in USD'].sum(
        )
        self.result_billing_amt_in_INR = self.project_details['Billing Amount in INR'].sum(
        )
        self.result_total_hrs_spent = self.project_details['Hours(For Calculation)'].sum(
        )
        # print(self.unique_employee, self.unique_tags, self.result_billing_amt_in_USR,
        #   self.result_billing_amt_in_INR, self.result_total_hrs_spent, sep='\n\n')

    def test_check_parameter(self):

        np.testing.assert_equal(
            self.unique_employee, pyTips.employee)
        np.testing.assert_equal(
            self.unique_tags, pyTips.tags)
        self.assertEqual(self.result_billing_amt_in_USR,
                         pyTips.billing_amt_in_USR)
        self.assertEqual(self.result_billing_amt_in_INR,
                         pyTips.billing_amt_in_INR)
        self.assertEqual(self.result_total_hrs_spent,
                         pyTips.total_hrs_spent)

    def test_calculate_activity_summary(self):
        result_calculate_activity_summary = pd.pivot_table(self.project_details, index=[
                                                           'Tag'], columns='User', values="Hours(For Calculation)", aggfunc=np.sum)
        assert_frame_equal(result_calculate_activity_summary,
                           pyTips.calculate_activity_summary())

    def test_calculate_employee_summary(self):
        result_calculate_employee_summary = self.project_details.groupby(
            'User').agg({'Hours(For Calculation)': 'sum'})
        assert_frame_equal(result_calculate_employee_summary,
                           pyTips.calculate_employee_summary())


if __name__ == '__main__':
    unittest.main()
