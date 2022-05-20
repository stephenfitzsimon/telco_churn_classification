# Telco Classification Project

## Introduction

This project explores the Telco data set to determine the variables of customer churn. It includes the full data science pipline: acquiring and cleaning the data, exploring and visualizing the data, and finally using a model to predict churn.

## Goals and Deliverables

- Goals
	- Identify at least 3 variables that predict churn
	- A model that is at least 0.75 accurate
	- A report communicating the data science pipeline process
- Deliverables
	- This readme
	- A final report Jupyter Notebook
	- Python modules automating the acquire and preparation of the data
	- A CSV of data predictions

## Process

#### Acquire and Prepare
- see acquire.py and prepare.py for full details on code, and acquire_prepare_notes.ipynb for more detailed notes
- foreign key columns were dropped 
- total_charges was cleaned and cast to float
- perpare.py contains split_telco_data() that will split the data into train, validate and test

#### Data Exploration
- Churned customers represent 0.27 of the data
- Churned customers seem to pay more per month
- Churned customers seem to have a lower tenure
- The categories with the highest churn are those having to do with payment type/plan, and having to do with a basic service.  In particular Fiber Optic Internet
- Customers who churned sometimes did not have an additional serivce such as online backup, or device protection

#### Hypothesis Testing

## Reproduction

## Key Findings

## Recommendations

## Final Takeaways

## Appendices

### Data Dictionary

### Custom Module descriptions

- acquire.py
	- get_telco_data(query_db=False) : Retrieves telco data either from the SQL database, or from 'telco.csv' in the current directory. query_db=True will force a database query, and overwrite any .csv file in the current directory
- prepare.py
	- prep_telco(df) : Drops unnecessary columns, drops null rows in the total_charges columns, and casts the total_charges type to float
	- split_telco_data(df) : takes the telco dataframe and returns train, validate and test dataframes
