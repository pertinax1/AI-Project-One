import dataframe_utils
import interactive_hvplot
import pandas as pd
import hvplot.pandas


__raw_binned_column_title = "col_to_bin"

__exlude_list = ["churn_after_treatment",\
                "churn_surv", \
                "cluster_bin", \
                "internet_monthly_charges_bin", \
                "phone_monthly_charges_bin", \
                "trigger_external", \
                "trigger_point_bin", \
                "trigger_price", \
                "trigger_quality"]

__save_images = True
__image_output_base_path = "output/images/"
__image_output_subfolder = "charts_for_presentation/"
__image_output_extension = ".png"

__save_ratio_dfs = False
__ratio_dfs_path = "output/churn_ratio_dfs/"
__ratio_dfs_extension = ".csv"

__print_ratio_dfs = False

__include_title = True

__debug = False

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
for ratio_df in ratio_dfs_list:

    x_value = ratio_df.index.name

    ignore = False
    for exlude_name in __exlude_list:
        if exlude_name == x_value:
            ignore = True
            break

    if ignore:
        pass
    else:
        save_name = f"{dataframe_utils.get_chrun_column_name()}_vs_{x_value}"

        if __include_title:
            title_name = interactive_hvplot.create_formatted_column_title(save_name)
        else:
            title_name = ""

        if ("_bin" in x_value) and \
        (x_value != "phone_min_bin") and \
        (x_value != "internet_min_bin"):
            ratio_df.index.rename(interactive_hvplot.create_formatted_column_title(x_value), inplace=True)

            plot = ratio_df.hvplot.line(y=dataframe_utils.get_chrun_column_name(), \
                                        title = title_name)
            if __debug:
                print("bin")
        else:
            ratio_df.index.rename(interactive_hvplot.create_formatted_column_title(x_value), inplace=True)
            #plot = ratio_df.hvplot.bar(y=dataframe_utils.get_chrun_column_name())
            plot = ratio_df.hvplot.bar(y=dataframe_utils.get_chrun_column_name(), \
                                        title = title_name)
            if __debug:
                print("not bin")
        
        if __save_images:
            hvplot.save(plot,f"{__image_output_base_path}{__image_output_subfolder}{save_name}{__image_output_extension}")
        
        if __save_ratio_dfs:
            ratio_df.to_csv(f"{__ratio_dfs_path}{x_value}{__ratio_dfs_extension}")
            
        if __print_ratio_dfs:
            print(ratio_df.head())