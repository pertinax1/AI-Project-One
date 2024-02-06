import pandas as pd


def compute_churn_ratio_discrete(note_churn_df):
    """
    This function takes a column of note from a data frame and the churn column from that data frame,
    and returns a data frame with the churn ratio for each discrete/unique entry in the original column.

    Note: churn ratio = churn sum/column count

    inputs:
        -note_churn_df: a data frame that contains just the column of interest and the churn value columns
    return:
        -churn_ratio_df: data frame that contains all the ratios for the discrete columns 
    """

    #drop na

    #get list of all the unique values

    #loop through the unique values and group by those values

        #sum the churn count
        # divide the churn count by the sum of the churn columns
        # could probably do this as part of the group by with a lamda and the agg function

    #recombine the specific value dfs to create the churn_ratio_df

    #TODO: set this to an actual value
    churn_ratio_df = None
    return churn_ratio_df
    
