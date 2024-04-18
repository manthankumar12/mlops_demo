import snowflake.connector
import pandas as pd
from snowflake.connector import DictCursor
 
def fetch_data():
    conn = snowflake.connector.connect(
        user="manthankumar",
        password="Ranamkr@1201",
        account="tq06422.ca-central-1.aws",
        role="ACCOUNTADMIN",
        warehouse="COMPUTE_wh",
        database="snowlens",
        schema="PUBLIC",
    )
 
    cur = conn.cursor(DictCursor)
    query = 'select * from "QUERY_HISTORY_TABLE"'
    cur.execute(query)
    data_fetch = cur.fetchall()
    df = pd.DataFrame(data_fetch)
    cur.close()
    conn.close()
    return df
 
# For local debugging
if __name__ == "__main__":
    df = fetch_data()
    print(df)
