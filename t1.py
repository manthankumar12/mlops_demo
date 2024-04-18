import snowflake.connector
import pandas as pd
from snowflake.connector import DictCursor
from snowflake.snowpark.session import Session 
from snowflake.snowpark.session import Session 
from snowflake.snowpark import DataFrame 
from snowflake.snowpark.functions import col
import json
 
def hello(session: Session) -> DataFrame:
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
    session = Session.builder.configs(json.load(
      open("/change_your_path/connection.json"))).create()
    print (hello (session).show())
