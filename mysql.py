#Import Packages
from sqlalchemy import create_engine
import pandas as pd 

#Set up connection to VM

MYSQL_HOSTNAME = '34.170.252.228'
MYSQL_USER = 'tenzin'
MYSQL_PASSWORD = '12345'
MYSQL_DATABASE = 'nutrition' 

#Connect to mysql in VM
connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'

db = create_engine(connection_string)

#Query in mysql
query = 'select * from nutrition.table1;'
df = pd.read_sql(query, con=db)

#Load in dataset
real_df = pd.read_csv('https://raw.githubusercontent.com/fantasydatapros/data/master/combine/combine00to20.csv')
real_df

#Push the df to the table in mysql in the VM
real_df.to_sql('fake_table', con=db, if_exists='replace')