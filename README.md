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
8. Final take-aways and future possibilities
9. Appendices
	1. Data Dictionary
	2. Module Descriptions
	3. Reproducing this project

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
- What other factors are important to churn? Are they service based factors? Are they demographic factors?

## Process

#### Acquire and Prepare
- Data is acquired from the CodeUp mySQL database using credentials stored in env.py
- see acquire.py and prepare.py for full details on code, and acquire_prepare_notes.ipynb for more detailed notes
- foreign key columns were dropped 
- total_charges was cleaned and cast to float
	- total_charges contained 11 rows that had `' '` as a value.  These all had `tenure = 0`; because there were few rows in a large dataset, they were dropped.  Another option would be to infer `total_charges = 0`
- prepare.py contains split_telco_data() that will split the data into train, validate and test

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
- Overall the best performer is the Decision tree
- The decision tree is 

## Key Findings
- Month-to-month contracts were a predictor of churn
- Churned customers tend to pay more
- A decision tree model most accurately 

## Recommendations

As stated in the discussion about choosing the best model, customers churn because their willingness to pay for the service they have is lower than their monthly payment.  However, any solution must also cost below the cost to replace the customer.  Some of the following could possibly meet business needs:

Easiest/immediate solutions:
- Offer discounts to current customers who are likely to churn. These can be based on the following:
    - Move to automatic billing, or a longer contract.
    - Demographic discounts (senior discount).
    - Loyalty discounts for x months with the company.
Intermediate solutions:
- Contact customers who are likely to churn and get them service that meets their need
    - Some may only need DSL level service.
    - Offer additional services (online backup, device protection, etc.) to customers who want to keep fiber optic.
Long term solutions:
- Partner with companies for a loyalty reward program.
- Offer intermediate levels of service; for example, DSL with discounted extras (online backup, technical help, etc).

## Final Takeaways and Future Possibilities

- High predictors of churn are the following:
    - Fiber optic service
    - Month-to-Month contracts
    - Electronic check payments
- Solutions:
    - Offer discounts to likely-to-churn customers
    - Offer additional services to customers
    
### Meeting the goals of the project
- The three major predictors of churn were Month-to-Month contracts, Fiber Optic service, and electronic checks
- The decision tree model is greater than $0.75$ accurate
- This report communicates these findings
    
### For further research
- This is a limited analysis, any future analysis should consider the relationship between additional services and churn (see appendix)
- Are demographic correlated with churn factors? For example, what customers are likely to have dependents/partners? Are these more likely to have fiber optic?

## Appendices

### Data Dictionary

#### Customer Identification and Demographic Data:
- Customer ID (String)
- Gender (Male/Female)
- Partner status (Bool)
- Dependent status (Bool)
- Senior citizen status (Bool)

#### Customer Relationship information:
- Tenure in months (float)
- Monthly charges (\$USD) (float)
- Total charges (\$USD) (float)
- Paperless Billing (Bool)
- Payment type (categorical)
- Phone Service, with service option columns:
    - Multiple lines : One Line, Multiple Lines, No Phone Service (categorical)
- Internet Service Type: Fiber Optic, DSL, None (categorical)
- Internet Service Option columns (all bool):
    - Online security
    - Online backup
    - Device protection
    - Tech support
    - Streaming TV
    - Streaming movies
- Churn status (bool)

### Custom Module descriptions

- acquire.py
	- get_telco_data(query_db=False) : Retrieves telco data either from the SQL database, or from 'telco.csv' in the current directory. query_db=True will force a database query, and overwrite any .csv file in the current directory
- prepare.py
	- prep_telco(df) : Drops unnecessary columns, drops null rows in the total_charges columns, and casts the total_charges type to float
	- split_telco_data(df) : takes the telco dataframe and returns train, validate and test dataframes
	- telco_make_dummies(df) : makes encoded variables for all of the non-numeric data

### Reproducing this project

In order to reproduce this project download `acquire.py`, `prepare.py`, and `final_report.ipnyb`. Then make an `env.py` modeled on the above `env_example.py`.  Then run the `final_report.ipnyb` file in Jupyter Notebook.