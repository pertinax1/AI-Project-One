import pandas as pd
import hvplot.pandas
import pandas as pd
import glob

__debug = True

# Format the csv file name so it's an easy to read column title
def create_formatted_column_title(csv_file):
    title = csv_file
    if '\\' in title:
        title = title.split('\\')[1].split('.')[0]
    title = title.replace('_bin', '')
    title = title.replace('_', ' ').title()    
    title = title.replace(' Ratio Dfs', '')
    return title

def create_interactive_plot(combined_df):
    # Drop the index column
    combined_df = combined_df.reset_index(drop=True)

    # Set index to column_title
    combined_df = combined_df.set_index('Selected Value')

    #create interactive bar plot and save it to a file for embedding
    plot = combined_df.hvplot(y='churn', x='variable', groupby='Selected Value', kind='bar', Title='Churn Statistics', grid = True, xlabel = "Selected Value", ylabel = "Churn", yformatter = '%.2f', fontscale=1.5, legend='top_right', width=600, height=500).opts(xrotation=45,show_grid=True,framewise=True, shared_axes=False) 
    hvplot.save(plot, 'output/interactive_plot.html')

    if __debug:
        # Print the combined dataframe
        print(combined_df.head())
        print(combined_df.tail())

        # Print the plot
        print(plot)

def create_interactive_plot_from_file_list():
# Loop through each CSV file and append its contents to the combined dataframe
# Format the csv file name and add it to the data frame as the column_title that
# the user will select in the interactive hvplot
    
    # Create an empty dataframe to store the combined data
    combined_df = pd.DataFrame()

    # Get a list of all CSV files in a directory
    csv_files = glob.glob('output/churn_ratio_dfs/*.csv')

    for csv_file in csv_files:
        current_csv_df = pd.read_csv(csv_file)   
        current_csv_df = current_csv_df.rename(columns={current_csv_df.columns[0]: 'variable'})
        column_title = create_formatted_column_title(csv_file)
        current_csv_df['Selected Value'] = column_title
        combined_df = pd.concat([combined_df, current_csv_df])

    create_interactive_plot(combined_df)

def create_interactive_plot_from_df_list(ratio_df_list):
    # Create an empty dataframe to store the combined data
    combined_df = pd.DataFrame()
    for ratio_df in ratio_df_list:
        column_title = create_formatted_column_title(ratio_df.index.name)
        current_df = ratio_df.reset_index()
        current_df = current_df.rename(columns={current_df.columns[0]: 'variable'})
        current_df['Selected Value'] = column_title
        combined_df = pd.concat([combined_df, current_df])
    
    create_interactive_plot(combined_df)

    '''
    ToDo:  Eliminate csv files for elements we don't want to include in the interactive plot.
        Change names of the csv files to be more descriptive if we want the drop down variable names to be better
        Look at X axis labels values 

    Issues:
        Churn after treatment       

    '''
