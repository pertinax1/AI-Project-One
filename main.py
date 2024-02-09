import dataframe_utils
import pandas as pd
import hvplot.pandas


__raw_binned_column_title = "col_to_bin"

def make_column_list(raw_data_df, binned_column_names_df):
    columns_to_exlude = binned_column_names_df[__raw_binned_column_title].tolist()
    columns_to_exlude.append(dataframe_utils.get_chrun_column_name())
    columns_to_exlude.append("tenure_9_bin")
    columns_to_exlude.append("uuid")
    columns_to_exlude.append("Unnamed: 0")

    list_of_columns = []
    for column_title in raw_data_df.columns:
        if column_title not in columns_to_exlude:
            list_of_columns.append(column_title)

    return list_of_columns


account_data_df = pd.read_csv("output/account_df.csv")
binned_columns = pd.read_csv("output/column_names_to_bin.csv")



list_of_columns = make_column_list(account_data_df, binned_columns)

ratio_dfs_list = dataframe_utils.create_churn_ratio_dataframes(account_data_df, list_of_columns)

#display data here, print, plot, etc
"""
for ratio_df in ratio_dfs_list:
    title_name = f"{dataframe_utils.get_chrun_column_name()} vs {ratio_df.index.name}"
    if "_bin" in ratio_df.index.name:
        plot = ratio_df.hvplot.line(y=dataframe_utils.get_chrun_column_name())
        print("bin")
    else:
        plot = ratio_df.hvplot.bar(y=dataframe_utils.get_chrun_column_name())
        print("not bin")
    hvplot.save(plot,f"output/images/bar_and_line/{title_name}.png")
    #print(ratio_df.head())
    #ratio_df.to_csv(f"output/churn_ratio_dfs/{ratio_df.index.name}.csv")
"""

"""
for ratio_df in ratio_dfs_list:
    if ratio_df.index.name == "phone_min_bin" or ratio_df.index.name == "internet_min_bin":
        title_name = f"{dataframe_utils.get_chrun_column_name()} vs {ratio_df.index.name}"
        plot = ratio_df.hvplot.bar(y=dataframe_utils.get_chrun_column_name())
        hvplot.save(plot,f"output/images/bar_and_line/{title_name}_bar.png")
"""
for ratio_df in ratio_dfs_list:
    print(ratio_df.head())