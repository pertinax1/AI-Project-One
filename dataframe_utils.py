import pandas as pd

__churn_column_name = "churn"

def __split_dataframe_into_columns_with_churn(input_churn_df, list_of_column_names):
    churn_df_list = []
    for column_name in list_of_column_names:
        churn_df_list.append(input_churn_df[[column_name, __churn_column_name]])
    
    return churn_df_list

def __compute_churn_ratio_dataframes(raw_churn_df_list):
    #loop through the raw_churn_dfs, and create a new df that is that data grouped by 
    #its unique rows and churn ratios, and add them to a list
    churn_ratio_df_list = []

    for churn_df in raw_churn_df_list:
        #drop na
        churn_non_null_df = churn_df.dropna()

        #groupby the column using the formula for the churn ratio
        check_name = churn_non_null_df.iloc[:,0].name
        if check_name != __churn_column_name:
            column_name = check_name
        else:
            column_name = churn_non_null_df.iloc[:,1].name

        #sum the churn 
        churn_sum_df = churn_non_null_df.groupby(by=churn_non_null_df[column_name]).sum()

        #get count of churn
        churn_count_df = churn_non_null_df.groupby(by=churn_non_null_df[column_name]).count()

        #divide sum of churn by churn count to get churn ratio
        churn_ratio_df = churn_sum_df/churn_count_df

        #append churn ratio df to list
        churn_ratio_df_list.append(churn_ratio_df)

    return churn_ratio_df_list


def create_churn_ratio_dataframes(input_churn_df, list_of_column_names):
    """
    This function takes a column of note from a data frame and the churn column from that data frame,
    and returns a data frame with the churn ratio for each discrete/unique entry in the original column.

    Note: churn ratio = churn sum/column count

    inputs:
        -note_churn_df: a data frame that contains the data we want to look through (columns of interest and the churn column)
        -list_of_column_names: a list of strings that contain the names of columns of note to look through
    return:
        -churn_ratio_df: data frame that contains all the ratios for the discrete columns 
    """

    #create a dataframe for each column of note and store in a list of dfs
    raw_churn_df_list = __split_dataframe_into_columns_with_churn(input_churn_df, list_of_column_names)

    #return a list of data frames with a column of interest and the churn ratio for each unique value in that dataframe
    return __compute_churn_ratio_dataframes(raw_churn_df_list)