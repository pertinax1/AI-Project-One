# Churn Analysis - Exploratory Data Analysis and Initial Machine Learning Baseline Model Using Logistic Regression

## Project 1 - ASU AI Course - 2/13/2023
### Team 3:
* David Gerhart
* Cody Cushing
* Doug Francis

### Overview
Using customer data provided by Grid Dynamics (see Data Source below), perform an Exploratory Data Analysis to generate charts to explore the impact of the various features of the data (data columns) on customer churn.  Since time permitted, we also performed an initial machine learning model, using logistic regression.

### Repository Files of Most Interest
| File                            | Description |
| ------------------------------------ | ------------------------------------------------|
| bokehffptyu49.html                   | Bokeh packages is used for interactive graphs for html output
| Dataframe_utils.py                   | Provides functions to group by the feature (data column) and return the average percentage of customer churns.
| histograms_for_binning.ipynb         | Generated initial historgrams for each feature (factor) to help guild the binning process. Holds the bin lists generated for each factor. Also bar graph for the binned data for comparison to initial histograms
| interactive_hvplot.py                | Provides the code to generate the html interactive plots. In order to do this, it reads in the individual feature dataframes, stacks them in the required format and then generates the html plots.
| main.py                           | Calls Dataframe_Util to generate dataframes for each factor containing average churn. Generates individual dataframes and plots for each of the features. Calls interactive_hvplot to generate the stated dataframe as well as generating the interactive HTML plots.  Note: Make sure to set the constants at the top of the file to activate / deactivate desirned features.
| ML_Churn_2.ipynb                  | Machine language logistic regression model generated. Includes splitting the data between test and train, z-score standardization of the data, training, and predictions across the test data.  Also includes performance evaluation, such as the "Confusion Matrix" and finally "Feature Importance".
| ------ Non Code Files -------- | ------------------------------------- 
| Phase One Proposal.PDF                     | Write up of mock proposal to company for the project
| Proposal.Docx                     | Initial proposal to instructors for our project. 
| Readme.md                         | This is the project readme file. It is also the file you are reading.
| Phase One Presentation.pdf   | The PDF contains our presentation which was presented on 2/13 to the class.


### Repository File Directory Structure
```
|
│   .gitignore
│   bokehffptyu49.html     
│   dataframe_utils.py     
│   histograms_for_binning.ipynb 
│   interactive_hvplot.py
│   main.py
│   ML_Churn_2.ipynb
│   Proposal draft.docx
│   Readme.md
│   Steps to create bins.docx
│
├───output
│   │   account_df.csv
│   │   account_df.xlsx
│   │   column_names_to_bin.csv
│   │
│   ├───churn_ratio_dfs
│   │       avg_monthly_bill_bin.csv
│   │       churn_after_treatment.csv
│   │       churn_surv.csv
│   │       cluster_bin.csv
│   │       contract_duration.csv
│   │       gender.csv
│   │       internet_min_bin.csv
│   │       internet_monthly_charges_bin.csv
│   │       internet_services.csv
│   │       number_customer_service_calls_bin.csv
│   │       payment_method.csv
│   │       phone_min_bin.csv
│   │       phone_monthly_charges_bin.csv
│   │       phone_services.csv
│   │       tenure_bin.csv
│   │       treatment.csv
│   │       trigger_external.csv
│   │       trigger_point_bin.csv
│   │       trigger_price.csv
│   │       trigger_quality.csv
│   │
│   └───images
│       ├───bar_and_line
│       │   │   churn vs avg_monthly_bill_bin.png
│       │   │   churn vs contract_duration.png
│       │   │   churn vs gender.png
│       │   │   churn vs internet_min_bin.png
│       │   │   churn vs internet_min_bin_bar.png
│       │   │   churn vs internet_services.png
│       │   │   churn vs number_customer_service_calls_bin.png
│       │   │   churn vs payment_method.png
│       │   │   churn vs phone_min_bin.png
│       │   │   churn vs phone_min_bin_bar.png
│       │   │   churn vs phone_services.png
│       │   │   churn vs tenure_bin.png
│       │   │   churn vs treatment.png
│       │   │
│       │   └───dont_use
│       │           churn vs churn_after_treatment.png
│       │           churn vs churn_surv.png
│       │           churn vs cluster_bin.png
│       │           churn vs internet_monthly_charges_bin.png
│       │           churn vs phone_monthly_charges_bin.png
│       │           churn vs trigger_external.png
│       │           churn vs trigger_point_bin.png
│       │           churn vs trigger_price.png
│       │           churn vs trigger_quality.png
│       │
│       └───line_only
│               ai_ambb.png
│               ai_churn_vs_gender.png
│               ai_c_cat.png
│               ai_c_cb.png
│               ai_c_cd.png
│               ai_c_cs.png
│               ai_c_imb.png
│               ai_c_ins.png
│               ai_c_ncscb.png
│               ai_c_pm.png
│               ai_c_pmb.png
│               ai_c_pmcb.png
│               ai_c_ps.png
│               ai_c_t.png
│               ai_c_tb.png
│               ai_c_te.png
│               ai_c_tp.png
│               ai_c_tq.png
│               ai_imcb.png
│               ai_tpb.png
│
├───Resources
│       account_predict_data.csv
│
└───__pycache__
        dataframe_utils.cpython-310.pyc

```



### Data Source
 GitHub Repo: griddynamics/ rnd-gcp-starter-kits https://github.com/griddynamics/rnd-gcp-starter-kits/tree/main


 ### Using the model and code
 1. Run "histograms_for_binning.ipynb". It is a stand along Jupyter Notebook. This generates the binned columns for use for subsequent processing.
 2. Run "main.py". Prior to running make sure to set the constants at the top of the file.
 3. Run ML_Churn_2.ipynb. This file generates the logistic regression model. It can be run top to bottom as is.

### Results and a Summary of the Analysis
Our analysis performed a Exploratory Data Analysis (EDA) to present the impact of various features on customer churn. Where needed, the data was binned in order to aggregate customer churns. Plots demonstrated several factors that had impact on customer churn. An initial See the class presentation called "Phase One Presentation.pdf". After initial EDA, a basic machine learning model using logistic regression was run. The result was an 88% prediction accuracy aross the test data set (which was 30% of our data). The accuracy was maintained wheather the model predicted a churn or not.  This was visually demonstrated using a heat map of the confusion matrix. Finally a feature importance graph was generated. this indicated that the most important factors for explaining customer churn were Internet Charges per Minute of Internet Usage, Internet Monthly Charges, Customer Tenure and Contract Duration. In the Internet Usage and Internet Monthly Charges were positively correlated with customer churn, that is as they went up, the churn went up as well. Conversely, Customer Tenure and Contract Duration were inversely associated with customer churns. As a customer's tenure increased, they were much less likely to churn.

### Works Citied
1. Gartner Group and “Leading on the Edge of Chaos”, E. Murphy and M. Murphy
2. ChatGPT used for ideas and code generation for the machine language model
3. “Closest” function which returns the closest bin range given the actual value is from https://www.geeksforgeeks.org/python-find-closest-number-to-k-in-given-list/
4. Data from GitHub Repo: griddynamics/ rnd-gcp-starter-kits
https://github.com/griddynamics/rnd-gcp-starter-kits/tree/main
5. Churn analytics in the technology and telecom industries using Google Vertex AI (https://blog.griddynamics.com/churn-analytics-in-the-technology-and-telecom-industries-using-google-vertex-ai-a-reference-notebook )
