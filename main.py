import dataframe_utils
import pandas as pd


def make_column_list(raw_data_df, columns_to_exclude_df):
    raw_data_df = pd.DataFrame()
    for column_title in raw_data_df.columns:

"""
TODO: The current scripts in here are for testing, remove if wanted
"""
binned_data_df = pd.read_csv("output/account_df.csv")

list_of_columns = ["gender", "contract_duration", "payment_method"]

ratio_dfs_list = dataframe_utils.create_churn_ratio_dataframes(test_df, list_of_columns)

for ratio_df in ratio_dfs_list:
    print(ratio_df.head())