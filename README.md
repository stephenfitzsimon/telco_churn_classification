# Telco Classification Project

## Quick Summary of README.md
- Q: Who is a customer that churns? A: Someone on a month-to-month contract, with fiber optic internet, and no additional service.
- Q: How to prevent churn? A: Many churning customers seem to have internet service that is expensive and does not meet their needs; try to save them some money by moving them to other service types or encourage them to take advantage of additional services that are offered by Telco.

## Contents of README.md:
1. Introduction
2. Goals and Deliverables
3. Initial Hypothesis/Questions
4. Process
6. Key Findings
7. Recommendations
8. Final take-aways
9. Appendices
	a. Data Dictionary
	b. Module Descriptions
	c. Reproducing this project

## Introduction

This project explores the Telco data set to determine the variables of customer churn. It includes the full data science pipline: acquiring and cleaning the data, exploring and visualizing the data, and finally using a model to predict churn.

## Goals and Deliverables

- Goals
	- Identify at least 3 variables that predict churn
	- A model that is at least 0.75 accurate
	- A report communicating the data science pipeline process
- Deliverables
	- This readme
	- A final report Jupyter Notebook with clean code
	- Python modules automating the acquire and preparation of the data
	- A CSV of data predictions

## Initial Hypothesis/Questions

- I expect that contract and payment types are the most important predictors of churn
	- People who pay more and see it every month are reminded of the money they are spending and can make a value judgement on whether or not they want to spend their money
- Are additional services important parts of churn?
	- Are people more reluctant to leave the company if they have certain services?

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
- The categories with high churn are likely dependent variables
- Churn customers likely pay more per month, and have a shorter tenure

#### Models
- The following are good candidates for models:
	- Random Forest with a max_depth of 9 and a min_sample_leaf of 9
	- Linear Regression with liblinear solver
	- Decision Tree with a max_depth of 4
	- K Nearest Neighbors with k = 17
- Overall the best performer is the Random Forest Model

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

### Reproducing this project