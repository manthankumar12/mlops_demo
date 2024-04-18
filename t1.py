import snowflake.connector
import pandas as pd
from snowflake.connector import DictCursor
from snowflake.snowpark.session import Session 
from snowflake.snowpark.session import Session 
from snowflake.snowpark import DataFrame 
from snowflake.snowpark.functions import col
import json
 
def hello(session: Session) -> DataFrame:
    df = session.sql('select * from "QUERY_HISTORY_TABLE"')
    df1 = df.collect()
    df1.write.save_as_table("my_table" , mode="overwrite" , table_type = "temporary")
    df2 = session.table("my_table").collect()
    return df2
 
# For local debugging
if __name__ == "__main__":
    session = Session.builder.configs(json.load(
      open("/change_your_path/connection.json"))).create()
    print (hello (session).show())
