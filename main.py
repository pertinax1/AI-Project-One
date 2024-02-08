import dataframe_utils
import pandas as pd

"""
TODO: The current scripts in here are for testing, remove if wanted
"""
test_df = pd.read_csv("personal_resources/account_predict_data.csv")
print(test_df.head())

list_of_columns = ["gender", "contract_duration", "payment_method"]

ratio_dfs_list = dataframe_utils.create_churn_ratio_dataframes(test_df, list_of_columns)

for ratio_df in ratio_dfs_list:
    print(ratio_df.head())