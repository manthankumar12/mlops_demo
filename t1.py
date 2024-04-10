import snowflake.connector
import pandas as pd
from snowflake.connector import connect, DictCursor

conn = snowflake.connector.connect(
    user='manthan.kumar@progressresidential.com',
    account='rentprogress',
    role='intern_ops_data_analysis',
    warehouse='adhoc_wh',
    database='snowlens',
    schema='demo',
    authenticator='externalbrowser' 
    )
cur=conn.cursor()

query = 'select * from "QUERY_HISTORY_TABLE"'
cur = conn.cursor(DictCursor)
cur.execute(query)
data_fetch = cur.fetchall()
df = pd.DataFrame(data_fetch)
print(df)

cur.close()
conn.close()


