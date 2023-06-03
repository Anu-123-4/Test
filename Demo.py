#this code is to generate reprt using pandas
#@editor: Anushree devadiga
#hi
import pandas as pd
import pyodbc as odbc
from datetime import datetime
print(odbc.drivers())
ConnectionString=odbc.connect(
    'Driver={ODBC Driver 17 for SQL Server};'
    'Server=Anushree\SQLEXPRESS;'
    'Database=AdventureWorks2019;'
    'Trusted_Connection=yes;'

)

Query=pd.read_sql_query(

    '''
    select businessentityid,passwordhash,rowguid
    from Person.password
    ''',
    ConnectionString
)

DF=pd.DataFrame(Query)
DF.to_csv(datetime.now().strftime("%y-%m-%d_%I-%M-%S-%p")+'-Sql user password data.csv',index=False)
