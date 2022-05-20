from env import get_db_url
import os
import pandas as pd

def get_telco_data(query_db = False):
    '''
    Returns the telco data as a dataframe.  If there is not saved .csv file present in the current
    directory, it will query the SQL database to retrieve the data.

    Args:
        query_db = False (bool) : forces a querying of the database, and overwrites any existing .csv
            file within the current directory
    '''
    filename = 'telco.csv'
    if os.path.isfile(filename) and not query_db:
        print('Returning saved csv file.')
        return pd.read_csv(filename)
    else:
        print('Querying database ... ')
        query = '''
            SELECT c.*, ct.contract_type, pt.payment_type, iso.internet_service_type
            FROM customers AS c
            JOIN contract_types AS ct USING (contract_type_id)
            JOIN payment_types AS pt USING (payment_type_id)
            JOIN internet_service_types AS iso USING (internet_service_type_id);
        '''
        df = pd.read_sql(query, get_db_url('telco_churn'))
        print('Got data from the SQL database')
        df.to_csv(filename)
        print('Saved dataframe as a .csv!')
        return df