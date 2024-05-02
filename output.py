import snowflake.connector
import pandas as pd
from snowflake.connector import DictCursor

conn = snowflake.connector.connect(
    user="manthan",
    password="Manthanrana123",
    account="ls31517.ap-southeast-1",
    role="ACCOUNTADMIN",
    warehouse="COMPUTE_WH",
    database="SNOWLENS",
    schema="DEMO",
)
cur = conn.cursor(DictCursor)

query = 'select * from "QUERY_HISTORY_TABLE"'
cur.execute(query)
data_fetch = cur.fetchall()
df = pd.DataFrame(data_fetch)
print(df)

cur.close()
conn.close()